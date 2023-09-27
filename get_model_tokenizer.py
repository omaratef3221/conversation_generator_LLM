from transformers import GPT2Tokenizer, TFGPT2Model, AutoModelForSeq2SeqLM, AutoTokenizer
import torch

def get_model_tokenizer():
    original_model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-base", torch_dtype=torch.float32)
    tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-base")
    return original_model, tokenizer