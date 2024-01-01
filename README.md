# Conversation Generator

## Overview
The Conversation Generator is a specialized tool designed for generating realistic dialogues or conversations between two individuals. It finely tunes large language models (LLMs) to achieve this, working with both original and custom-tuned versions of various cutting-edge models.

## Supported Models
This tool supports and has been tested with the following original models:
- [google/flan-t5-base](https://huggingface.co/google/flan-t5-base)
- [bigscience/bloom-560m](https://huggingface.co/bigscience/bloom-560m)
- [microsoft/phi-2](https://huggingface.co/microsoft/phi-2)

Additionally, you can find the fine-tuned versions of these models, created specifically for dialogue generation, at these Hugging Face links:
- [Omaratef3221/phi2-dialogue-generator](https://huggingface.co/Omaratef3221/phi2-dialogue-generator)
- [Omaratef3221/flan-t5-base-dialogue-generator](https://huggingface.co/Omaratef3221/flan-t5-base-dialogue-generator)

## Installation Requirements
Ensure a smooth operation of the Conversation Generator with the following dependencies:
- `transformers==4.36.2`
- `datasets==2.10.1`

## Getting Started
1. **Clone the Repository**: Clone this repository to your local machine or development environment.
2. **Install Dependencies**: Run `pip install -r requirements.txt` to install the necessary libraries.
3. **Set Up Your Huggingface Credentials**: Configure your Huggingface credentials for seamless integration and access to models.
4. **Run Training Script**: Execute `train.py` to start the Adam-optimized training process.

## Dataset
Training uses the [Kaggle Dialogue Dataset](https://www.kaggle.com/datasets/sukalp1899/dialog-summarization), ideal for conversational model tuning.

## Contributing
Contributions are welcome. Feel free to fork, modify, and submit a pull request. Open an issue for any suggestions or problems.

## Contact
📧 Email: [omaratef3221@gmail.com](mailto:omaratef3221@gmail.com)

🐦 Twitter: [@OmarAtef3221](https://twitter.com/OmarAtef3221)
