from uuid import UUID

from sqlalchemy import ForeignKey, String, Uuid
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.models.base import UUIDTimestampMixin


class Lead(UUIDTimestampMixin, Base):
    __tablename__ = "leads"

    restaurant_id: Mapped[UUID] = mapped_column(
        Uuid(as_uuid=True), ForeignKey("restaurants.id", ondelete="CASCADE"), unique=True, nullable=False
    )
    assigned_user_id: Mapped[UUID | None] = mapped_column(
        Uuid(as_uuid=True), ForeignKey("users.id", ondelete="SET NULL"), index=True
    )
    status: Mapped[str] = mapped_column(String(50), nullable=False, default="new", index=True)

    restaurant: Mapped["Restaurant"] = relationship(back_populates="lead")
    assigned_user: Mapped["User | None"] = relationship(back_populates="assigned_leads")
    interactions: Mapped[list["Interaction"]] = relationship(back_populates="lead")
