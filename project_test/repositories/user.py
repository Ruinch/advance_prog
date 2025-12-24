# repositories/user.py

from sqlalchemy.orm import Session
from sqlalchemy import select

from models.user import User


class UserRepository:
    """
    Repository layer for User model.
    Handles all database operations related to users.
    """

    def __init__(self, db: Session) -> None:
        self.db = db

    def get_by_id(self, user_id: int) -> User | None:
        stmt = select(User).where(User.id == user_id)
        return self.db.scalar(stmt)

    def get_by_email(self, email: str) -> User | None:
        stmt = select(User).where(User.email == email)
        return self.db.scalar(stmt)

    def create(self, *, email: str, password_hash: str, role: str = "user") -> User:
        user = User(
            email=email,
            password_hash=password_hash,
            role=role,
        )
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def delete(self, user: User) -> None:
        self.db.delete(user)
        self.db.commit()

    def list(self, *, skip: int = 0, limit: int = 100) -> list[User]:
        stmt = select(User).offset(skip).limit(limit)
        return list(self.db.scalars(stmt))
