# api/v1/auth.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from core.database import get_db
from services.auth import AuthService
from schemas.user import UserCreate, UserRead, Token
from core.exceptions import (
    UserAlreadyExistsError,
    InvalidCredentialsError,
    InactiveUserError,
)

router = APIRouter()


@router.post(
    "/register",
    response_model=UserRead,
    status_code=status.HTTP_201_CREATED,
)
def register(
    user_in: UserCreate,
    db: Session = Depends(get_db),
) -> UserRead:
    """
    Register a new user.
    """
    service = AuthService(db)

    try:
        user = service.register(
            email=user_in.email,
            password=user_in.password,
        )
        return user
    except UserAlreadyExistsError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email already exists",
        )


@router.post(
    "/login",
    response_model=Token,
)
def login(
    user_in: UserCreate,
    db: Session = Depends(get_db),
) -> Token:
    """
    Authenticate user and return JWT tokens.
    """
    service = AuthService(db)

    try:
        tokens = service.login(
            email=user_in.email,
            password=user_in.password,
        )
        return tokens
    except InvalidCredentialsError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
        )
    except InactiveUserError:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="User account is inactive",
        )
