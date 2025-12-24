# main.py

from fastapi import FastAPI

from core.config import settings
from core.database import init_db
from api.v1 import router as api_router

app = FastAPI(
    title=settings.app_name,
    version="1.0.0",
    description="Secure User Management REST API",
)


@app.on_event("startup")
def on_startup() -> None:
    """
    Initialize application resources.
    """
    init_db()


app.include_router(api_router, prefix="/api/v1")


@app.get("/", tags=["Health"])
def health_check() -> dict[str, str]:
    return {"status": "ok"}
