import enum

from sqlalchemy import Enum, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.models.base import UUIDTimestampMixin


class UserRole(str, enum.Enum):
    ADMIN = "admin"
    COMMERCIAL = "commercial"
    ANALYST = "analyst"


class User(UUIDTimestampMixin, Base):
    __tablename__ = "users"

    full_name: Mapped[str] = mapped_column(String(255), nullable=False)
    email: Mapped[str] = mapped_column(String(320), nullable=False, unique=True)
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)
    role: Mapped[UserRole] = mapped_column(
        Enum(UserRole, name="user_role"), nullable=False, default=UserRole.COMMERCIAL
    )

    assigned_leads: Mapped[list["Lead"]] = relationship(back_populates="assigned_user")
