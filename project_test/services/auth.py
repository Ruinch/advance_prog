# services/auth.py

from sqlalchemy.orm import Session

from repositories.user import UserRepository
from core.security import (
    hash_password,
    verify_password,
    create_access_token,
    create_refresh_token,
)
from core.exceptions import (
    UserAlreadyExistsError,
    UserNotFoundError,
    InvalidCredentialsError,
    InactiveUserError,
)
from models.user import User


class AuthService:
    """
    Authentication service.
    Handles user registration and login logic.
    """

    def __init__(self, db: Session) -> None:
        self.user_repo = UserRepository(db)

    def register(self, *, email: str, password: str) -> User:
        """
        Register a new user.
        """
        existing_user = self.user_repo.get_by_email(email)
        if existing_user:
            raise UserAlreadyExistsError()

        password_hash = hash_password(password)

        user = self.user_repo.create(
            email=email,
            password_hash=password_hash,
        )
        return user

    def login(self, *, email: str, password: str) -> dict[str, str]:
        """
        Authenticate user and return JWT tokens.
        """
        user = self.user_repo.get_by_email(email)
        if user is None:
            raise InvalidCredentialsError()

        if not user.is_active:
            raise InactiveUserError()

        if not verify_password(password, user.password_hash):
            raise InvalidCredentialsError()

        access_token = create_access_token(subject=str(user.id))
        refresh_token = create_refresh_token(subject=str(user.id))

        return {
            "access_token": access_token,
            "refresh_token": refresh_token,
        }

    def get_user(self, user_id: int) -> User:
        """
        Retrieve user by ID.
        """
        user = self.user_repo.get_by_id(user_id)
        if user is None:
            raise UserNotFoundError()
        return user
