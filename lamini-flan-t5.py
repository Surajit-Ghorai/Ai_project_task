# model: LaMini-Flan-T5-783M  source: hugging face
# result: best performance so far. good at enhancing facts, researchbook name recommendation is bad, could be better than this.

from transformers import pipeline

checkpoint = "MBZUAI/LaMini-Flan-T5-783M"

model = pipeline('text2text-generation', model = checkpoint)

# fact enhancement
facts= [
    "The accused did not create or submit forged documents to the authority.",
    "Physical or mental torture.",
    "Loan pending with the bank.",
    "The defendant was seen leaving the crime scene at the time of the incident."
]

for fact in facts:
    input_text = f"rewrite the following sentence in a formal legal tone: {fact}"
    generated_text = model(input_text, max_length=512, do_sample=True)[0]['generated_text']
    print("Enhanced fact: ", generated_text)

# researchbook name recommendation
facts= [
    "Siblings Murder",
    "Cheque Bounce",
    "Murder",
    "Is a last will considered the final will of a person?"
]

for fact in facts:
    input_text = f"recommend me a legal book or document related to : {fact}"
    generated_text = model(input_text, max_length=512, do_sample=True, temperature= 0.9)[0]['generated_text']
    print("Researchbook : ", generated_text)