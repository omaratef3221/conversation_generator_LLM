import pandas as pd
from datasets import Dataset
from get_model_tokenizer import get_model_tokenizer
train_data_df = pd.read_csv("train.csv")[["dialogue", "summary"]]
validation_data_df = pd.read_csv("validation.csv")[["dialogue", "summary"]]
test_data_df = pd.read_csv("test.csv")[["dialogue", "summary"]]

data_df = pd.concat([train_data_df, validation_data_df, test_data_df],axis=0)

data = Dataset.from_pandas(data_df)

_, tokenizer = get_model_tokenizer()

def tokenize_function(example):
    start_prompt = '\n\nGenerate a dialogue between two people about the following topic:\n'
    end_prompt = '\n\nDialogue:\n'
    prompt = [start_prompt + s + end_prompt for s in example["summary"]]
    example['input_ids'] = tokenizer(prompt, padding="max_length", truncation=True, return_tensors="pt").input_ids
    example['labels'] = tokenizer(example["dialogue"], padding="max_length", truncation=True, return_tensors="pt").input_ids
    return example

def get_dataset(print_info = True):
    tokenized_datasets = data.map(tokenize_function, batched=True)
    tokenized_datasets = tokenized_datasets.remove_columns(['dialogue', 'summary',])
    if print_info:
        print("Dataset Info: ")
        print("Dataframe sample: ")
        print(data_df.head(4))
        print("Dataset Details")
        print(tokenized_datasets)
        print("=="*30)
    return tokenized_datasets

