# Custom Thought Callback Handler For Language Model Agents
This project provides a `ThoughtCallbackHandler` class that extends `BaseCallbackHandler` for handling callbacks in a Language Model (LM) execution context. It allows you to display the output of an LM along with intermediate results history.

## Installation
1. Clone the repository.
2. Install the required dependencies.

## Usage
To use `ThoughtCallbackHandler`, simply import the class and create an instance:

```python
from thought_callback_handler import ThoughtCallbackHandler
...
callback_handler = ThoughtCallbackHandler()
```

Then, pass this `callback_handler` to your LM or agent, and it will handle the callbacks accordingly. For instance:

```python
response = executor.run({"input":payload, "chat_history":chat_history}, callbacks=[callback_handler])
```

## Accessing Thought and Code History
The `ThoughtCallbackHandler` maintains a history of thoughts and codes encountered during the execution of the Language Model. This is accomplished through the `history` attribute, which is updated each time a new action is processed or when the chain of thought ends. These histories can be helpful for understanding the sequence of operations and decisions made by the Language Model, aiding in debugging and performance optimization.

## Integrating with Streamlit
Though `ThoughtCallbackHandler` can function standalone, it's also designed with extensibility in mind and can be integrated with interactive tools such as Streamlit.

To leverage Streamlit's real-time updating functionality, you can pass a custom Streamlit callback handler to the `ThoughtCallbackHandler`. This custom Streamlit callback handler can be designed to take the thought and code histories at each end of the step and display it on a Streamlit component. 

## License
This project is licensed under the MIT License.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any bugs, improvements, or features.
