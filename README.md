# Conversation Generator

## Overview
The Conversation Generator is a specialized tool designed to fine-tune large language models (LLMs) for generating realistic dialogues or conversations between two individuals. It is capable of working with various cutting-edge models, making it highly versatile and effective for a wide range of conversational scenarios.

## Supported Models
This tool has been tested and is compatible with the following models:
- [google/flan-t5-base](https://huggingface.co/google/flan-t5-base): An advanced T5 model by Google, known for its effectiveness in understanding and generating human-like text.
- [bigscience/bloom-560m](https://huggingface.co/bigscience/bloom-560m): A robust model from BigScience, offering a balance between size and performance.
- [microsoft/phi-2](https://huggingface.co/microsoft/phi-2): Microsoft's PHI-2 model, renowned for its language understanding and generation capabilities.

## Installation Requirements
To ensure smooth operation of the Conversation Generator, please install the following dependencies:
- `transformers==4.36.2`: Provides the backbone for working with the aforementioned LLMs.
- `datasets==2.10.1`: Essential for handling various datasets, including the one used in this project.

## Getting Started
To begin fine-tuning the models, follow these steps:
1. **Clone the Repository**: Clone this repository to your local machine or development environment.
2. **Install Dependencies**: Run `pip install -r requirements.txt` to install the necessary libraries.
3. **Set Up Your Huggingface Credentials**: For seamless integration and access to models, configure your Huggingface credentials.
4. **Run Training Script**: Execute the `train.py` script to start the training process. The script utilizes the Adam optimizer for effective training.

## Dataset
The training utilizes the [Kaggle Dialogue Dataset](https://www.kaggle.com/datasets/sukalp1899/dialog-summarization), a comprehensive collection of dialogues ideal for fine-tuning conversational models.

## Contributing
Contributions to improve the Conversation Generator are welcome. Feel free to fork the repository, make changes, and submit a pull request.

---

For any issues or suggestions, please open an issue in this repository. Your feedback is invaluable in enhancing this tool.
