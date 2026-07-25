from datetime import datetime
from uuid import UUID

from sqlalchemy import DateTime, ForeignKey, String, Text, Uuid, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.models.base import UUIDTimestampMixin


class Interaction(UUIDTimestampMixin, Base):
    __tablename__ = "interactions"

    lead_id: Mapped[UUID] = mapped_column(
        Uuid(as_uuid=True), ForeignKey("leads.id", ondelete="CASCADE"), nullable=False, index=True
    )
    interaction_type: Mapped[str] = mapped_column(String(50), nullable=False, index=True)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    occurred_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now(), index=True
    )

    lead: Mapped["Lead"] = relationship(back_populates="interactions")
