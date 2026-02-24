from fastapi import APIRouter
from app.models.chat_models import ChatRequest, ChatResponse

router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    return ChatResponse(
        answer=f"You said: {request.message}",
        confidence=0.95
    )