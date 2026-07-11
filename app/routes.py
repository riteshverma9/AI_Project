"""API route definitions."""

from fastapi import APIRouter, HTTPException

from app.logger import get_logger
from app.models import ChatRequest, ChatResponse, HealthResponse
from app.services import ChatService

router = APIRouter()
logger = get_logger(__name__)


@router.get("/api/health", response_model=HealthResponse)
async def health_check() -> HealthResponse:
    """Simple health check endpoint."""
    return HealthResponse(status="ok")


@router.post("/api/chat", response_model=ChatResponse)
async def chat(request: ChatRequest) -> ChatResponse:
    """Accept a user message and return an AI-generated reply."""
    try:
        reply = ChatService.get_reply(request.message)
        return ChatResponse(reply=reply)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    except Exception as exc:
        logger.exception("Chat request failed")
        raise HTTPException(
            status_code=502, detail="AI provider request failed"
        ) from exc
