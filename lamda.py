# pip install transformers

import google.api_core.exceptions
from google.cloud import language_v1

client = language_v1.LanguageServiceClient()

def generate_enhanced_facts_with_lamda(facts):
    document = language_v1.Document(content=facts, type_=language_v1.Document.Type.PLAIN_TEXT)

    # Construct a LaMDA query with a clear prompt for legal context
    query_input = language_v1.Document(
        content="Explain the significance of these facts in a legal setting, adding relevant context and implications:\n" + facts
    )

    try:
        response = client.annotate_text(
            request={"document": document, "features": {"extract_syntax": True}, "query": query_input}
        )

        # Access and process LaMDA's generated text
        enhanced_facts = response.query_result.fulfillment_text

        return enhanced_facts

    except google.api_core.exceptions.GoogleAPICallError as error:
        print("Request failed with error: {}".format(error))
        return None
    
# Example usage
facts=[
    "The accused did not create or submit forged documents to the authority.",
    "Physical or mental torture.",
    "Loan pending with the bank.",
    "The defendant was seen leaving the crime scene at the time of the incident."
]
for fact in facts:
    enhanced_fact = generate_enhanced_facts_with_lamda(fact)

    print(f"Original facts: {fact}")
    print(f"Enhanced facts: {enhanced_fact}")
    print("\n")

