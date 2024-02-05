from transformers import pipeline

checkpoint = "MBZUAI/LaMini-GPT-1.5B"

model = pipeline('text2text-generation', model = checkpoint)

facts= [
    "The accused did not create or submit forged documents to the authority.",
    "Physical or mental torture.",
    "Loan pending with the bank.",
    "The defendant was seen leaving the crime scene at the time of the incident."
]

for fact in facts:
    input_text = f"rewrite the following sentence in a formal legal tone.\n\n### Instruction:\n{fact}\n\n### Response:"
    generated_text = model(input_text, max_length=512, do_sample=True)[0]['generated_text']
    print("Enhanced fact: ", generated_text)


facts= [
    "Siblings Murder",
    "Cheque Bounce",
    "Murder",
    "Is a last will considered the final will of a person?"
]

for fact in facts:
    input_text = input_text = f"recommend me a legal book or document related to the following instruction.\n\n### Instruction:\n{fact}\n\n### Response:"
    generated_text = model(input_text, max_length=512, do_sample=True, temperature= 0.9)[0]['generated_text']
    print("Researchbook : ", generated_text)