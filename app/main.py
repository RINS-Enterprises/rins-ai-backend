from fastapi import FastAPI
from app.routes.chat import router as chat_router

app = FastAPI(
    title="RINS AI Backend",
    description="FastAPI backend for AI integrations and conversational APIs.",
    version="1.0.0"
)

app.include_router(chat_router)


@app.get("/")
def root():
    return {"message": "RINS AI Backend Running"}