# pip install bardapi

from bardapi import Bard

import os

os.environ["_BARD_API_KEY"] = "g.a000fwjzJIrCHqFXVcLT6XgGFsslkfRUh-zv_R831nLpU3iflyMq4fD06K9XP3PeTxm2AcPJ_AACgYKAWwSAQASFQHGX2Mi3eGzwowAb7SXJFNzCaUSbhoVAUF8yKrX6MV5WU3nVeU-c_o8bWkn0076"

# function for fact enhancement
def call_bard(prompt):
    input_text = f"""
    Reconstruct the following sentence in a formal, legal tone, add few legal terms if required: {fact}

    sample examples:

        * Fact: "Loan pending with the bank."
        * Enhanced Fact: "A loan is pending with a bank."

        * Fact: "Physical or mental torture."
        * Enhanced Fact: "The victim suffered from torture, whether physical or mental."

        * Fact: "The accused did not create or submit forged documents to the authority."
        * Enhanced Fact: "The defendant did not produce or present falsified records to the governing body."

    now just reply the enhanced fact for the given fact like above examples, don't add any breakdown or explaination.
    """

    enhanced_fact = Bard().get_answer(input_text=input_text)
    return enhanced_fact

# function for researchbook recommendation
def call_bard2(query):
    # Prompt with placeholder for legal query
    prompt = f'''
      I'm a lawyer. i have received a case related to {query}.
      now i need to research on that topic or similar cases. for that i need book recommendation related to law.
      so recommend me a book on: {query}
      example:

        Query: "Siblings Murder"
        Research Book Name: " Analyzing Murder Cases: Relevant Judgments and Legal Insights "

        Query: " Cheque Bounce "
        Research Book Name: " Cheque Bounce Chronicles: Legal Perspectives and Summaries "

        Query: " Murder "
        Research Book Name: "Understanding Sibling Murder Cases: Relevant Judgments and Legal Strategies"

        Query: " Is a last will considered the final will of a person? "
        Research Book Name: " Finality of Last Wills: Legal Implications and Precedents"
    '''

    output = Bard().get_answer(query)

    return output

# enhancing facts
facts=[
    "Deepfake video used in online fraud.",
    "drink and drive.",
    "he was accused of taking bribe.",
]

for fact in facts:
    enhanced_fact = call_bard(fact)
    enhanced_fact = enhanced_fact["content"]
    print(f"fact:{fact}")
    print(f"Enhanced Fact: \"{enhanced_fact}\"\n")

# researchbook name
queries = [
    "Siblings Murder",
    "Cheque Bounce",
    "Murder",
    "Is a last will considered the final will of a person?"
]

for query in queries:
    research_book_name = call_bard2(query)
    print(f"Query: \"{query}\"\n Research Book Name: \"{research_book_name}\"\n")
