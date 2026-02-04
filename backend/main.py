from fastapi import FastAPI
from pydantic import BaseModel

from generate import generate_response

app = FastAPI(
    title="AI Customer Support API",
    version="1.0.0"
)


# Request schema
class ChatRequest(BaseModel):
    question: str


# API endpoint
@app.post("/chat")
def chat(request: ChatRequest):

    answer = generate_response(request.question)

    return {
        "status": "success",
        "question": request.question,
        "answer": answer
    }