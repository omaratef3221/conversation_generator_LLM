from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, GenerationConfig
import torch
from peft import PeftModel, PeftConfig



peft_model_path="./dialouge_generator"

model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-base", torch_dtype=torch.float32)
tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-base")

peft_model = PeftModel.from_pretrained(model, 
                                       peft_model_path, 
                                       torch_dtype=torch.float32,
                                       is_trainable=False)


peft_model.push_to_hub("Dialouge_generator")

original_model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-base", 
                                                       torch_dtype=torch.float32,)

tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-base")

def generate_conversation(text, model):
    if text == "exit":
        return "closed"
    start_prompt = '\n\nGenerate a dialogue between two people about the following topic:\n'
    end_prompt = '\n\nDialogue:\n'
    prompt = start_prompt + text + end_prompt
    tokenized_statement = tokenizer([prompt], return_tensors= 'pt')
    
    

    ## Fine tuned model
    outputs_ft = peft_model.generate(input_ids=tokenized_statement["input_ids"], 
                                  generation_config=GenerationConfig(max_new_tokens=200, num_beams=3),
                                  top_k = 10, temperature = 1, do_sample = True
                                    )
    
   
    final_output_ft = tokenizer.decode(outputs_ft[0], skip_special_tokens=True)
    ###############
    
    ## Original model
    op = original_model.generate(input_ids=tokenized_statement["input_ids"], 
                                      generation_config=GenerationConfig(max_new_tokens=200, num_beams=1),
                                        top_k = 30, temperature = 1)
    
    
    # print("\nAnswers: ")
    # print("\nOriginal Model:", tokenizer.decode(op[0], skip_special_tokens=True).replace(".", "\n"))
    # print("\nT5 Fine-Tuned: ", final_output_ft.replace(".", "\n"))
    # print("="*30)
    return final_output_ft.replace(".", "\n")
