"""Business logic layer sitting between routes and the AI client."""

from app.ai import generate_reply
from app.logger import get_logger
from app.utils import timed

logger = get_logger(__name__)


class ChatService:
    """Encapsulates chat-related business logic."""

    @staticmethod
    @timed
    def get_reply(message: str) -> str:
        """Return an AI-generated reply for the given user message."""
        message = message.strip()
        if not message:
            raise ValueError("Message cannot be empty.")
        logger.info("Processing chat message (%d chars)", len(message))
        return generate_reply(message)
