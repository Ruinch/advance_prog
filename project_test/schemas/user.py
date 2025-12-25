# schemas/user.py

from datetime import datetime
from pydantic import BaseModel, EmailStr, Field


class UserBase(BaseModel):
    """
    Shared user fields.
    """
    email: EmailStr
    role: str = Field(default="user")


class UserCreate(UserBase):
    """
    Schema for user registration.
    """
    password: str = Field(min_length=8, max_length=128)


class UserLogin(BaseModel):
    """
    Schema for user authentication.
    """
    email: EmailStr
    password: str


class UserRead(UserBase):
    """
    Schema for returning user data via API.
    """
    id: int
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True


class Token(BaseModel):
    """
    JWT token response schema.
    """
    access_token: str
    refresh_token: str
    token_type: str = "bearer"
