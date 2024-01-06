# Conversation Generator

## Overview 🌟
The Conversation Generator is a specialized tool designed for generating realistic dialogues or conversations between two individuals. It finely tunes large language models (LLMs) to achieve this, working with both original and custom-tuned versions of various cutting-edge models.

## Supported Models 🚀
This tool supports and has been tested with the following original models:
- 🌐 [google/flan-t5-base](https://huggingface.co/google/flan-t5-base) - An advanced T5 model by Google, known for its effectiveness in generating human-like text.

### Fine-Tuned Models 🎯
Check out the fine-tuned versions for dialogue generation and try them out on 🤗:
- 🌐 [Omaratef3221/flan-t5-base-dialogue-generator](https://huggingface.co/Omaratef3221/flan-t5-base-dialogue-generator)

## Complete Example


## Installation Requirements 🛠️
Ensure a smooth operation of the Conversation Generator with the following dependencies:
- `pip install transformers==4.36.2`
- `pip install datasets==2.10.1`

## Getting Started 🔍
1. **Clone the Repository**: Clone this repository to your local machine or development environment.
2. **Set Up Your Huggingface Credentials**: Configure your Huggingface credentials for seamless integration and access to models.
3. **Run Training Script**: Execute `train.py` to start the Adam-optimized training process.

## Dataset 📚
Training uses the [Kaggle Dialogue Dataset](https://www.kaggle.com/datasets/sukalp1899/dialog-summarization), ideal for conversational model tuning.

## Website Interface for Local Testing 💻
The `website` folder contains a basic web interface for locally testing the model. It includes HTML, CSS, and JavaScript files that create a user-friendly front-end to interact with the model. To set this up:

1. **Start the Flask API**: Ensure the `python_api.py` file in the parent directory is running. it contains the Flask API needed to handle requests from the website.
2. **Navigate to the Website Folder**: `cd website`
3. **Open `home.html`**: Open the HTML file in a web browser to access the interface.
4. **Interact with the Model**: Use the interface to send requests to the Flask API, which in turn communicates with the Conversation Generator model.

Make sure that the Flask API in `python_api.py` is correctly configured to receive requests from the web interface and to communicate with the model.

## Contributing 🤝
Contributions are welcome. Feel free to fork, modify, and submit a pull request. Open an issue for any suggestions or problems.

## Contact 📩
- 📧 Email: [omaratef3221@gmail.com](mailto:omaratef3221@gmail.com)
- 🐦 Twitter: [@OmarAtef3221](https://twitter.com/OmarAtef3221)
