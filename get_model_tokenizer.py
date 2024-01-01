from transformers import GPT2Tokenizer, TFGPT2Model, AutoModelForSeq2SeqLM, AutoTokenizer
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch


def get_model_tokenizer(model = 't5'):
    if model == 't5':
        original_model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-base", torch_dtype=torch.float16)
        tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-base")
        return original_model, tokenizer
    elif model == 'bloom':
        tokenizer = AutoTokenizer.from_pretrained("bigscience/bloom-560m")
        original_model = AutoModelForCausalLM.from_pretrained("bigscience/bloom-560m")
        return original_model, tokenizer
    elif model == 'phi2':
        original_model = AutoModelForCausalLM.from_pretrained("microsoft/phi-2", torch_dtype="auto", trust_remote_code=True)
        tokenizer = AutoTokenizer.from_pretrained("microsoft/phi-2", trust_remote_code=True)
        return original_model, tokenizer