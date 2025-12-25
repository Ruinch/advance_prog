# api/v1/users.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core.database import get_db
from core.security import get_current_user, require_admin
from models.user import User
from repositories.user import UserRepository
from schemas.user import UserRead


router = APIRouter()


@router.get(
    "/me",
    response_model=UserRead,
    summary="Get current authenticated user",
)
def read_current_user(
    current_user: User = Depends(get_current_user),
) -> User:
    """
    Returns data of the currently authenticated user.
    """
    return current_user


@router.get(
    "/",
    response_model=list[UserRead],
    summary="Get all users (admin only)",
)
def read_all_users(
    db: Session = Depends(get_db),
    _: User = Depends(require_admin),
) -> list[User]:
    """
    Returns list of all users.
    Accessible only for admin users.
    """
    return UserRepository(db).get_all()
