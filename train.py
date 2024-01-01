from transformers import GenerationConfig, TrainingArguments, Trainer
from peft import LoraConfig, get_peft_model, TaskType
import torch
import torch
from dataset import get_dataset
from get_model_tokenizer import get_model_tokenizer
import time
import os
from huggingface_hub import login


## Hyper Parameters and other parameters
EPOCHS = 25
PRINT_INFO = True
LR = 1e-4
BATCH_SIZE = 4
#########

model_name = 'phi2'
model, tokenizer = get_model_tokenizer(model = model_name)
model.to("cuda")

# Get the dataset
training_data = get_dataset(print_info=PRINT_INFO)

def print_number_of_trainable_model_parameters(model):
    trainable_model_params = 0
    all_model_params = 0
    for _, param in model.named_parameters():
        all_model_params += param.numel()
        if param.requires_grad:
            trainable_model_params += param.numel()
    return f"trainable model parameters: {trainable_model_params}\nall model parameters: {all_model_params}\npercentage of trainable model parameters: {100 * trainable_model_params / all_model_params:.2f}%"

if PRINT_INFO:
    print("="*30)
    print(print_number_of_trainable_model_parameters(model))


training_output_dir = f'./{model_name}_dialogue_generator-{str(int(time.time()))}'



training_args = TrainingArguments(
    output_dir=training_output_dir,
    overwrite_output_dir=True,
    auto_find_batch_size=True,
    learning_rate=LR, 
    num_train_epochs=EPOCHS,
    per_device_train_batch_size=BATCH_SIZE,
    logging_steps=1,
    logging_strategy = 'epoch',
    max_steps=-1, 
    fp16=True,

    push_to_hub = True,
    hub_model_id = f'{model_name}-dialogue-generator',
    hub_token = '<YOUR TOKEN>',
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=training_data,
)

trainer.train()

model_path=f"./{model_name}_dialogue_generator"

trainer.model.save_pretrained(model_path)
tokenizer.save_pretrained(model_path)


login('<YOUR TOKEN>')
repo_name = f'{model_name}-dialogue-generator'

tokenizer.push_to_hub()

if PRINT_INFO:
    print("="*30)
    print("Training Done and Model saved at: ", model_path)
    print("="*30)
