# pip install transformers

from transformers import T5Tokenizer, T5ForConditionalGeneration

tokenizer = T5Tokenizer.from_pretrained("google/flan-t5-base")
model = T5ForConditionalGeneration.from_pretrained("google/flan-t5-base")

# fact enhancement
def generate_enhanced_facts_with_t5(fact, model_name="google/flan-t5-base"):
  # Load the tokenizer and model
  tokenizer = T5Tokenizer.from_pretrained(model_name)
  model = T5ForConditionalGeneration.from_pretrained(model_name)

  # Prepare the input text with a prompt
  input_text = f"Explain this fact in a legal context, adding relevant details and implications and concequences : {fact}"

  # Encode the input text
  #input_ids = tokenizer.encode(input_text, return_tensors="pt")
  input_ids = tokenizer(input_text, return_tensors="pt").input_ids

  # Generate enhanced facts
  #'''
  output = model.generate(
      input_ids,
      max_length=512,  # Adjust desired maximum length
      num_beams=4,  # Adjust beam search width
      early_stopping=True,
      do_sample=True,
      top_p=0.9,
      temperature =0.7,
      no_repeat_ngram_size=2,
  )
  '''
  output = model.generate(
      input_ids,
  )'''

  # Decode the generated text
  #enhanced_facts = tokenizer.decode(output[0], skip_special_tokens=True).split("\n")
  outputs = model.generate(input_ids)
  enhanced_facts = tokenizer.decode(outputs[0])

  # Remove empty strings and the prompt from the output
  #enhanced_facts = [fact.strip() for fact in enhanced_facts if fact.strip()]

  return enhanced_facts

