from datetime import datetime
from uuid import UUID

from sqlalchemy import DateTime, ForeignKey, Integer, String, Text, Uuid, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.models.base import UUIDTimestampMixin


class Source(UUIDTimestampMixin, Base):
    __tablename__ = "sources"

    restaurant_id: Mapped[UUID] = mapped_column(
        Uuid(as_uuid=True), ForeignKey("restaurants.id", ondelete="CASCADE"), nullable=False, index=True
    )
    source_type: Mapped[str] = mapped_column(String(100), nullable=False, index=True)
    source_url: Mapped[str | None] = mapped_column(Text)
    confidence: Mapped[int | None] = mapped_column(Integer)
    collected_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )

    restaurant: Mapped["Restaurant"] = relationship(back_populates="sources")
