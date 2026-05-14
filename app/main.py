import os
from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")

app = FastAPI(
    title="RINS AI Backend",
    description="FastAPI backend for AI integrations and conversational APIs.",
    version="1.0.0"
)

class ChatRequest(BaseModel):
    message: str

@app.get("/")
def root():
    return {"message": "RINS AI Backend Running"}

@app.post("/chat")
def chat(request: ChatRequest):
    response = model.generate_content(request.message)

    return {
        "user_message": request.message,
        "ai_response": response.text
    }