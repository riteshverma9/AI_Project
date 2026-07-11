"""Generic utility helpers."""

import time
from functools import wraps
from typing import Any, Callable

from app.logger import get_logger

logger = get_logger(__name__)


def timed(func: Callable) -> Callable:
    """Decorator that logs the execution time of a function."""

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        logger.info("%s executed in %.3fs", func.__name__, elapsed)
        return result

    return wrapper


def truncate(text: str, max_length: int = 200) -> str:
    """Truncate text to a maximum length, appending an ellipsis if needed."""
    if len(text) <= max_length:
        return text
    return text[: max_length - 3] + "..."
