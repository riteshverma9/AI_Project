"""FastAPI application entry point for AI_Project."""

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.config import get_settings
from app.logger import get_logger
from app.routes import router

settings = get_settings()
logger = get_logger(__name__)

app = FastAPI(title=settings.APP_NAME, version="1.0.0")

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

app.include_router(router)


@app.get("/", response_class=HTMLResponse)
async def index(request: Request) -> HTMLResponse:
    """Serve the chat UI."""
    return templates.TemplateResponse(
        request, "index.html", {"app_name": settings.APP_NAME}
    )


if __name__ == "__main__":
    import uvicorn

    logger.info(
        "Starting %s on %s:%s", settings.APP_NAME, settings.APP_HOST, settings.APP_PORT
    )
    uvicorn.run("main:app", host=settings.APP_HOST, port=settings.APP_PORT, reload=True)
