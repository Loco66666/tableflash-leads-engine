from sqlalchemy import func, select
from sqlalchemy.orm import Session
from uuid import UUID

from app.models.user import User


class UserRepository:
    def __init__(self, session: Session) -> None:
        self.session = session

    def count(self) -> int:
        return self.session.scalar(select(func.count()).select_from(User)) or 0

    def get_by_email(self, email: str) -> User | None:
        return self.session.scalar(select(User).where(User.email == email.lower()))

    def get_by_id(self, user_id: UUID) -> User | None:
        return self.session.get(User, user_id)

    def create(self, user: User) -> User:
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user
