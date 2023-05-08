from typing import Any, Dict, List, Optional, Union
import streamlit as st
import json
import re

from langchain.callbacks.streamlit import BaseCallbackHandler
from langchain.schema import AgentAction, AgentFinish, LLMResult


class StreamlitThoughtCallbackHandler(BaseCallbackHandler):
    def __init__(self, response_area: st.empty, thought_area: st.empty) -> None:
        """Initialize the callback handler with two empty Streamlit areas."""
        self.response_area = response_area
        self.thought_area = thought_area
        self.tokens_stream = ""

        self.thought_stream = []
        self.code_stream = []

        self.final = False
        self.answer = False
        self.start_signal = False

    def on_llm_new_token(self, token: str, **kwargs: Any) -> None:
        """Handle new LLM token when streaming is enabled."""
        if "Final" in token:
            self.final = True
        if "Answer" in token:
            self.answer = True
        if '":' in token and self.final and self.answer:
            self.start_signal = True

        if self.final and self.answer and self.start_signal:
            token = re.sub(r'[|":|"|{|}|`]', '', token)
            self.tokens_stream += token
            self.tokens_stream = self.tokens_stream.replace("\\n", "\n")
            self.response_area.markdown(self.tokens_stream)

    def on_llm_end(self, response: LLMResult, **kwargs: Any) -> None:
        """Reset state and clear response area on LLM end."""
        self.response_area.write("")
        self.tokens_stream = ""
        self.final = False
        self.answer = False
        self.start_signal = False

    def on_agent_action(self, action: AgentAction, **kwargs: Any) -> Any:
        """Display action information in the corresponding area."""
        action_name = action.tool
        action_input = action.tool_input

        if action_name == "python_repl_ast":
            self.code_stream.append(action_input)
            self._generate_code_history_tabs()

    def on_chain_end(self, outputs: Dict[str, Any], **kwargs: Any) -> None:
        """Display the chain of thought on chain end."""
        output_text = outputs.get("text", "")
        if "Final Answer" in output_text:
            return None

        if "```" in output_text:
            clean_output_text = self._clean_output_text(output_text)
            self.thought_stream.append(clean_output_text)
            self._generate_code_history_tabs()

    def _clean_output_text(self, output_text: str) -> str:
        """Convert JSON blob in output text to a readable code block."""
        def replace_json(match):
            json_blob = match.group(1)
            data = json.loads(json_blob)

            tool_name = data.get("action", "")
            tool_input_string = data.get("action_input", "")

            return f"## {tool_name}\n```\n{tool_input_string}\n```\n"

        cleaned_output = re.sub(r'```json\n(.*?)\n```', replace_json, output_text, flags=re.DOTALL)
        return cleaned_output

    def _generate_code_history_tabs(self):
        """Generate code history tabs in the Streamlit app."""
        n_tabs = len(self.thought_stream)
        code_history_tabs = self.thought_area.tabs([f"History ({n_tabs-i}/{n_tabs})" for i in range(n_tabs)])
        for i, code_tab in enumerate(code_history_tabs[::-1]):
            code_tab.markdown
