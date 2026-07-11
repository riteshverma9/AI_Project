"""Pydantic request/response models."""

from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    """Incoming chat message from the client."""

    message: str = Field(..., min_length=1, description="User message")


class ChatResponse(BaseModel):
    """Outgoing AI-generated reply."""

    reply: str = Field(..., description="AI generated response")


class HealthResponse(BaseModel):
    """Health check response."""

    status: str = "ok"
