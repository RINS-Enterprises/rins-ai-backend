# RINS AI Backend

FastAPI-based AI backend for conversational APIs, AI integrations, and backend engineering experiments.

## Features

- FastAPI backend architecture
- Gemini AI integration
- REST API endpoints
- Swagger/OpenAPI documentation
- Environment variable management
- JSON request/response handling

## Tech Stack

- Python
- FastAPI
- Gemini API
- Uvicorn
- Pydantic

## API Endpoints

### GET /

Health check endpoint.

### POST /chat

Send a message to the AI model.

Example request:

```json
{
  "message": "Explain APIs simply"
}
```

## Run Locally

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## API Documentation

Swagger UI available at:

```text
http://127.0.0.1:8000/docs
```

## Future Improvements

- PostgreSQL integration
- JWT authentication
- Dockerization
- Async processing
- Logging middleware
- Conversation history storage