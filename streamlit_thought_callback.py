from typing import Any, Dict, List, Optional, Union, Callable
import streamlit as st
from copy import copy
import json
import re

from langchain.callbacks.streamlit import BaseCallbackHandler
from langchain.schema import AgentAction, AgentFinish, LLMResult


class ThoughtsCallbackHandler(BaseCallbackHandler):
    """ Return intermediate agent thoughts and actions. """
    history = []

    def __init__(self, streamlit_callback: Callable = None):
        """
        Parameters
        ----------
        streamlit_callback : function that receives the live intermediate step history
        """
        self.streamlit_callback = streamlit_callback
        super().__init__()

    def on_agent_action(
        self, action: AgentAction, color: Optional[str] = None, **kwargs: Any
    ) -> Any:
        """Run on agent action."""
        action_name = action.tool
        action_input = action.tool_input

        if action_name == "python_repl_ast":
            if action_name == "python_repl_ast":
                if isinstance(action_input, dict):
                    action_input = action_input["action_input"]
                    thought = ''
                else:
                    if "action:" in action.log.lower():
                        thought = action.log[: action.log.lower().find("action:")]
                    else:
                        thought = action.log

                self.history.append({'thought': thought, 'code': action_input})
                if self.streamlit_callback is not None:
                    self.streamlit_callback(self.history)

    def reset_history(self):
        self.history = []

    def get_history(self):
        return copy(self.history)
