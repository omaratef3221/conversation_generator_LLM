from transformers import GenerationConfig, TrainingArguments, Trainer
from peft import LoraConfig, get_peft_model, TaskType
import torch
import torch
from dataset import get_dataset
from get_model_tokenizer import get_model_tokenizer
import time
import os
os.environ["TOKENIZERS_PARALLELISM"] = "false"

## Hyper Parameters and other parameters
EPOCHS = 25
PRINT_INFO = True
LR = 1e-4
BATCH_SIZE = 8
#########

model, tokenizer = get_model_tokenizer(model = 'bloom')
model.to("mps")

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


training_output_dir = f'./bloom560m_dialogue_generator-{str(int(time.time()))}'



training_args = TrainingArguments(
    output_dir=training_output_dir,
    overwrite_output_dir=True,
    auto_find_batch_size=True,
    learning_rate=LR, 
    num_train_epochs=10,
    per_device_train_batch_size=BATCH_SIZE,
    logging_steps=1,
    logging_strategy = 'epoch',
    max_steps=-1, 
    use_mps_device= True,
    push_to_hub = True,
    hub_model_id = 'bloom-560m-dialogue-generator',
    hub_token = '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',
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=training_data,
)

trainer.train()

model_path="./bloom560m_dialogue_generator"

trainer.model.save_pretrained(model_path)
tokenizer.save_pretrained(model_path)

if PRINT_INFO:
    print("="*30)
    print("Training Done and Model saved at: ", model_path)
    print("="*30)
