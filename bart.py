# pip install transformers

# Import libraries
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Load pre-trained BART model and tokenizer
model_name = "facebook/bart-base"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

# Function to generate enhanced legal facts
def generate_enhanced_facts_with_bart(facts):
  # Prepare input text with start and end tokens
  input_text = f"Input facts: {facts} \n </s> \n Generate enhanced facts: "
  '''
  input_text = f"Facts: {facts} \nPrompt: Explain the significance of these facts in a legal setting, adding relevant context and implications: "
  '''

  # Encode the input text
  input_ids = tokenizer.encode(input_text, return_tensors="pt")

  # Generate text using beam search
  '''
  output = model.generate(
      input_ids,
      max_length=256,  # Adjust desired max length
      num_beams=4,  # Adjust beam search width
      early_stopping=True,
      do_sample=True,
      top_p=0.9,
      no_repeat_ngram_size=2,
  )
'''
  output = model.generate(
      input_ids,
      max_length=1024,  # Adjust desired max length
      num_beams=8,  # Adjust beam search width
      early_stopping=False,
      do_sample=True,
      top_p=1,
      temperature=0.6,
      no_repeat_ngram_size=2,
  )

  # Decode the generated text
  enhanced_facts = tokenizer.decode(output[0], skip_special_tokens=True)

  return enhanced_facts

# Example usage
facts=[
    "The accused did not created or submitting forged documents on the authority.",
    "Physical or mental torture.",
    "Loan pending with the bank.",
    "The defendant was seen leaving the crime scene at the time of the incident."
]
for fact in facts:
    enhanced_fact = generate_enhanced_facts_with_bart(fact)

    print(f"Original facts: {fact}")
    print(f"Enhanced facts: {enhanced_fact}")
    print("\n")

# researchbook name generation
def generate_research_book_name_with_bart(query):
    input_text = f"generate a legal book name or document name and its author, related to : {query}"
    input_ids = tokenizer.encode(input_text, return_tensors="pt")

    output = model.generate(
      input_ids,
    )

    # Decode the generated text
    research_book_name = tokenizer.decode(output[0], skip_special_tokens=True)

    return research_book_name

queries = [
    "Siblings Murder",
    "Cheque Bounce",
    "Murder",
    "Is a last will considered the final will of a person?"
]

for query in queries:
    research_book_name = generate_research_book_name_with_bart(query)
    print(f"Query: \"{query}\"\n Research Book Name: \"{research_book_name}\"\n")