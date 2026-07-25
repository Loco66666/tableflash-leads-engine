from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.auth.repository import UserRepository
from app.auth.schemas import UserCreate
from app.auth.security import hash_password, verify_password
from app.models.user import User, UserRole


class AuthService:
    def __init__(self, session: Session) -> None:
        self.repository = UserRepository(session)

    def create_user(self, payload: UserCreate, actor: User | None) -> User:
        is_bootstrap = self.repository.count() == 0
        if not is_bootstrap and (actor is None or actor.role != UserRole.ADMIN):
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Administrator access required")
        if self.repository.get_by_email(payload.email):
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Email already exists")

        user = User(
            full_name=payload.full_name,
            email=payload.email.lower(),
            password_hash=hash_password(payload.password),
            role=UserRole.ADMIN if is_bootstrap else payload.role,
        )
        return self.repository.create(user)

    def authenticate(self, email: str, password: str) -> User:
        user = self.repository.get_by_email(email)
        if user is None or not verify_password(password, user.password_hash):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
        return user
