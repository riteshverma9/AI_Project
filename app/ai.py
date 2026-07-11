"""AI client integration - NVIDIA (OpenAI-compatible API)."""

from openai import OpenAI

from app.config import get_settings
from app.logger import get_logger

settings = get_settings()
logger = get_logger(__name__)

client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key="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",
)

DEFAULT_MODEL = "deepseek-ai/deepseek-v4-pro"


def generate_reply(message: str) -> str:
    """Send a message to the NVIDIA AI endpoint and return the reply text."""
    try:
        response = client.chat.completions.create(
            model=DEFAULT_MODEL,
            messages=[{"role": "user", "content": message}],
            temperature=0.7,
            max_tokens=1024,
        )
        return response.choices[0].message.content or ""
    except Exception as exc:
        logger.error("NVIDIA AI request failed: %s", exc)
        raise
