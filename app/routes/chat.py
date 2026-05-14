from fastapi import APIRouter
from app.schemas.chat import ChatRequest
from app.services.gemini_service import generate_ai_response

router = APIRouter()


@router.post("/chat")
def chat(request: ChatRequest):
    ai_response = generate_ai_response(request.message)

    return {
        "user_message": request.message,
        "ai_response": ai_response
    }