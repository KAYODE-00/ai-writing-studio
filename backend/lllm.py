from groq import Groq
from config import GROQ_API_KEY,MODEL

client = Groq(api_key=GROQ_API_KEY)

def ask_llm(message,temperature=0.2):

    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        temperature=temperature
    )

    return response.choices[0].message.content