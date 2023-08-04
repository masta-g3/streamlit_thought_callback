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

## License
This project is licensed under the MIT License.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any bugs, improvements, or features.
