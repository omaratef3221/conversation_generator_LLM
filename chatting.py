from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, GenerationConfig, AutoModelForCausalLM
import torch


original_model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-base")


def generate_conversation(text, model = 't5'):
  if model == 't5':
    tokenizer = AutoTokenizer.from_pretrained("Omaratef3221/flan-t5-base-dialogue-generator")
    model = AutoModelForSeq2SeqLM.from_pretrained("Omaratef3221/flan-t5-base-dialogue-generator")
  elif model == "phi2":
    tokenizer = AutoTokenizer.from_pretrained("Omaratef3221/bloom-560m-dialogue-generator")
    model = AutoModelForCausalLM.from_pretrained("Omaratef3221/bloom-560m-dialogue-generator")

  else:
    raise Exception(f"model {model} is not yet supported")
  if text == "exit":
      return "closed"
  start_prompt = '\n\nGenerate a dialogue between two people about the following topic:\n'
  end_prompt = '\n\nDialogue:\n'
  prompt = start_prompt + text + end_prompt
  tokenized_statement = tokenizer([prompt], return_tensors= 'pt')
  
  

  ## Fine tuned model
  outputs_ft = model.generate(input_ids=tokenized_statement["input_ids"], 
                                generation_config=GenerationConfig(num_beams=1),
                                top_k = 10, temperature = 0.5, max_length = 100
                                  )
  
  
  final_output_ft = tokenizer.decode(outputs_ft[0], skip_special_tokens=True)
  ###############
  
  ## Original model
  op = original_model.generate(input_ids=tokenized_statement["input_ids"], 
                                    generation_config=GenerationConfig(max_new_tokens=100, num_beams=1),
                                      top_k = 10, temperature = 1)
  
  
  # print("\nAnswers: ")
  # print("\nOriginal Model:", tokenizer.decode(op[0], skip_special_tokens=True).replace(".", "\n"))

  # print("\nT5 Fine-Tuned: ", final_output_ft.replace(".", "\n"))
  # print("="*30)
  return final_output_ft.replace(".", "\n").replace('"', "")