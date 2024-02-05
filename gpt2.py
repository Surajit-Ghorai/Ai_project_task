import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel


def generate_research_book_name(query, model_name="gpt2"):
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)
    model = GPT2LMHeadModel.from_pretrained(model_name)

    input_text = "Query: \"" + query + ". Now give me a reasearch or legal book name related to query."
    input_ids = tokenizer.encode(input_text, return_tensors="pt")

    # Get pad_token_id from model configuration
    pad_token_id = tokenizer.eos_token_id if tokenizer.eos_token_id is not None else tokenizer.pad_token_id

    # Explicitly set attention_mask and pad_token_id
    attention_mask = input_ids.ne(pad_token_id)
    output = model.generate(input_ids, max_length=100, num_return_sequences=1, no_repeat_ngram_size=2, attention_mask=attention_mask, pad_token_id=pad_token_id)

    research_book_name = tokenizer.decode(output[0], skip_special_tokens=True)

    return research_book_name

# Examples
queries = [
    "Siblings Murder",
    "Cheque Bounce",
    "Murder",
    "Is a last will considered the final will of a person?"
]

for query in queries:
    research_book_name = generate_research_book_name(query)
    print('\n')
    print(f"Query: \"{query}\"\n Research Book Name: \"{research_book_name}\"\n")

# enhancing fact
print('\n')    

def generate_enhanced_facts(fact, model_name="gpt2"):
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)
    model = GPT2LMHeadModel.from_pretrained(model_name)

    # input_text = "Fact: \"" + fact + "\"\n Enhanced Fact: \""
    input_text = "Rewrite this fact in a formal, legal tone: \"" + fact + "\n"
    # input_text = f"here is a fact: {fact}. Rewrite this fact in a formal, legal tone, and in one sentence, similar to these examples: \n fact :\"Loan pending with the bank\" to enhanced legal fact: \"A loan is pending with a bank.\" \n fact: \"Physical or mental torture\" to enhanced legal fact: \"The victim suffered from torture, whether physical or mental.\" \n fact: \"The accused did not create or submit forged documents to the authority\" to enhanced legal fact: \"The defendant did not produce or present falsified records to the governing body.\"\n"
    # print(input_text)

    input_ids = tokenizer.encode(input_text, return_tensors="pt")

    # Get pad_token_id from model configuration
    pad_token_id = tokenizer.eos_token_id if tokenizer.eos_token_id is not None else tokenizer.pad_token_id

    # Explicitly set attention_mask and pad_token_id
    attention_mask = input_ids.ne(pad_token_id)
    output = model.generate(input_ids, max_length=400, num_return_sequences=1, no_repeat_ngram_size=2, attention_mask=attention_mask, pad_token_id=pad_token_id)

    enhanced_fact = tokenizer.decode(output[0], skip_special_tokens=True)

    return enhanced_fact

# Examples
facts = [
    "The witness report contradicted the defendant's alibi, casting doubt on his claims of innocence."
]

for fact in facts:
    enhanced_fact = generate_enhanced_facts(fact)
    print("\n>>>>>>>")
    print(f"fact:{fact} \n")
    print(f"Enhanced Fact: \"{enhanced_fact}\"\n")