"""Application configuration loaded from environment variables."""

import os
from functools import lru_cache

from dotenv import load_dotenv

load_dotenv()


class Settings:
    """Centralized application settings."""

    APP_NAME: str = os.getenv("APP_NAME", "AI_Project")
    APP_ENV: str = os.getenv("APP_ENV", "development")
    APP_HOST: str = os.getenv("APP_HOST", "0.0.0.0")
    APP_PORT: int = int(os.getenv("APP_PORT", "8000"))
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")

    AI_PROVIDER: str = "NVIDIA"
    NVIDIA_API_KEY: str = os.getenv("NVIDIA_API_KEY", "")


@lru_cache
def get_settings() -> Settings:
    """Return a cached Settings instance."""
    return Settings()
