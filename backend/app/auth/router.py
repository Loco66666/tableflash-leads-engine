from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.auth.dependencies import get_current_user, get_optional_current_user
from app.auth.schemas import LoginRequest, TokenResponse, UserCreate, UserRead
from app.auth.security import create_access_token
from app.auth.service import AuthService
from app.db.session import get_db
from app.models.user import User

router = APIRouter(prefix="/auth", tags=["authentication"])


@router.post("/users", response_model=UserRead, status_code=status.HTTP_201_CREATED)
def create_user(
    payload: UserCreate,
    session: Session = Depends(get_db),
    actor: User | None = Depends(get_optional_current_user),
) -> UserRead:
    return AuthService(session).create_user(payload, actor)


@router.post("/login", response_model=TokenResponse)
def login(payload: LoginRequest, session: Session = Depends(get_db)) -> TokenResponse:
    user = AuthService(session).authenticate(payload.email, payload.password)
    return TokenResponse(access_token=create_access_token(user.id), user=user)


@router.get("/me", response_model=UserRead)
def get_me(current_user: User = Depends(get_current_user)) -> UserRead:
    return current_user
