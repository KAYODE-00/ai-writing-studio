from llm import ask_llm

STORE_INFORMATION = """
Store name: Qay's Store

Delivery:
Orders usually arrive within 3-5 business days.

Refund policy:
Customers can request a refund within 7 days
of receiving their order.

Payment:
We accept bank transfers and card payments.
"""

def generate_response(question):

    system_prompt = f"""
    You are a professional customer support assistant.

    Your job is to answer customer questions politely.

    Use only the store information provided below.

    If the information does not contain the answer,
    tell the customer to contact human support.

    Store information:
    {STORE_INFORMATION}
    """

    messages = [
        {
            "role": "system",
            "content": system_prompt
        },
        {
            "role": "user",
            "content": question
        }
    ]

    response = ask_llm(messages)

    return response