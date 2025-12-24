# core/config.py

from functools import lru_cache
from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    """
    Central application configuration.
    Loaded from environment variables or .env file.
    """

    # Application
    app_name: str = "Secure User Management API"
    debug: bool = False

    # Database
    database_url: str = Field(
        default="sqlite:///./app.db",
        description="Database connection URL",
    )

    # JWT
    jwt_secret_key: str = Field(
        ...,
        description="Secret key for JWT token signing",
    )
    jwt_algorithm: str = "HS256"
    access_token_expire_minutes: int = 15
    refresh_token_expire_minutes: int = 60 * 24 * 7  # 7 days

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True


@lru_cache
def get_settings() -> Settings:
    """
    Cached settings instance.
    Prevents re-reading environment variables multiple times.
    """
    return Settings()


settings = get_settings()
