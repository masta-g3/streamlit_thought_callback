# Custom Streamlit Thought Callback For Langchain Agents

This project provides a `StreamlitThoughtCallbackHandler` class that extends `BaseCallbackHandler` for handling callbacks in a Streamlit application. It allows you to display the streamling output of an LLM (Language Model) along with intermediate results history.

## Installation

1. Clone the repository.
2. Install the required dependencies.

## Usage

To use `StreamlitThoughtCallbackHandler` in your Streamlit application, simply import the class and create an instance with two empty Streamlit areas:

```python
from streamlit_thought_callback import StreamlitThoughtCallbackHandler
import streamlit as st

response_area = st.empty()
thought_area = st.empty()

...

callback_handler = StreamlitThoughtCallbackHandler(response_area, thought_area)
```

Then, pass this callback_handler to your LLM or agent, and it will handle the callbacks accordingly. I.e.:

```python
response = executor.run({"input":payload, "chat_history":chat_history}, callbacks=[callback_handler])
```

## License
This project is licensed under the MIT License.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any bugs, improvements, or features.