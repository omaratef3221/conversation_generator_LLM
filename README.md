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

Here's a complete example showing how to use the Conversation Generator for generating dialogues:

```python
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

model_name = "Omaratef3221/flan-t5-base-dialogue-generator"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

prompt = '''
Generate a dialogue between two people about the following topic:
A local street market bustles with activity, #Person1# tries exotic food for the first time, and #Person2#, familiar with the cuisine, offers insights and recommendations.
Dialogue:
'''

# Generate a response to an input statement
input_ids = tokenizer(prompt, return_tensors='pt').input_ids
output = model.generate(input_ids, top_p=0.6, do_sample=True, temperature=1.2, max_length=512)
print(tokenizer.decode(output[0], skip_special_tokens=True).replace('#Person2#:', '\n#Person2#:').replace('#Person1#:', '\n#Person1#:'))
```
### output:
```python
#Person1#: Oh, that's a nice street market. I'm glad I got to see it. 
#Person2#: Yes, it is. I like the food here. 
#Person1#: And the prices are reasonable. 
#Person2#: I have been to this street market before, and I like it very much. 
#Person1#: I'm impressed. I really like it. 
#Person2#: I'm familiar with the cuisine. It is one of the best in the world. 
#Person1#: What kind of food do you like? 
#Person2#: I like Italian food, but I like Thai food. 
#Person1#: Oh, that's really exciting. I like it very much. I think I'll take it. 
#Person2#: I like Thai food too. 
#Person1#: What's your favorite food? 
#Person2#: I'm familiar with Thai food. I love spicy food, but I don't like spicy food. 
#Person1#: Is that true? 
#Person2#: Yes, that's right. 
#Person1#: I like spicy food too. How about Thai food? 
#Person2#: That's a great idea. I think it's really good. 
#Person1#: Oh, that's a good idea. What's your favorite restaurant? 
#Person2#: Oh, I'm sure I can recommend it. 
#Person1#: I like Thai food, too. What do you recommend? 
#Person2#: It's a very popular restaurant in China. 
#Person1#: Oh, that's great. 
#Person2#: I would like to try it. 
#Person1#: Thanks. I'll try it.
```

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
