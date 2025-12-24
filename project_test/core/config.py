# core/config.py

from functools import lru_cache
from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Central application configuration.
    """

    # Application
    app_name: str = "Secure User Management API"
    debug: bool = False

    # Database
    DATABASE_URL: str = Field(
        default="sqlite:///./app.db",
        description="Database connection URL",
    )

    # JWT
    JWT_SECRET_KEY: str = Field(
        ...,
        description="Secret key for JWT token signing",
    )
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 15
    REFRESH_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7

    model_config = {
        "env_file": ".env",
        "env_file_encoding": "utf-8",
        "extra": "ignore",  # ← КЛЮЧЕВО
    }


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
