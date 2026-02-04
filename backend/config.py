import os
from dotenv import load_dotenv  
load.dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

MODEL = os.getenv(
    "GROQ_MODEL",
    "model_id"
)


APP_NAME = "AI Customer support assistant"

SUPPORT_EMAIL = "qaymail00@gmail.com"
STORE_NAME = "Qay's store"