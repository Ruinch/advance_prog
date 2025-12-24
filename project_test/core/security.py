# core/security.py

from datetime import datetime, timedelta
from typing import Any

from jose import jwt, JWTError
from passlib.context import CryptContext

from core.config import settings


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    """
    Hash a plain password using bcrypt.
    """
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verify a plain password against its hash.
    """
    return pwd_context.verify(plain_password, hashed_password)


def _create_token(
    *, subject: str, expires_delta: timedelta, token_type: str
) -> str:
    """
    Internal helper to create JWT tokens.
    """
    payload: dict[str, Any] = {
        "sub": subject,
        "type": token_type,
        "exp": datetime.utcnow() + expires_delta,
        "iat": datetime.utcnow(),
    }
    return jwt.encode(
        payload,
        settings.jwt_secret_key,
        algorithm=settings.jwt_algorithm,
    )


def create_access_token(subject: str) -> str:
    """
    Create JWT access token.
    """
    expires = timedelta(minutes=settings.access_token_expire_minutes)
    return _create_token(
        subject=subject,
        expires_delta=expires,
        token_type="access",
    )


def create_refresh_token(subject: str) -> str:
    """
    Create JWT refresh token.
    """
    expires = timedelta(minutes=settings.refresh_token_expire_minutes)
    return _create_token(
        subject=subject,
        expires_delta=expires,
        token_type="refresh",
    )


def decode_token(token: str) -> dict[str, Any]:
    """
    Decode and validate JWT token.
    """
    try:
        payload = jwt.decode(
            token,
            settings.jwt_secret_key,
            algorithms=[settings.jwt_algorithm],
        )
        return payload
    except JWTError as exc:
        raise ValueError("Invalid or expired token") from exc
