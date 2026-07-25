from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.models.base import UUIDTimestampMixin


class Restaurant(UUIDTimestampMixin, Base):
    __tablename__ = "restaurants"

    name: Mapped[str] = mapped_column(String(255), nullable=False, index=True)
    address: Mapped[str | None] = mapped_column(Text)
    city: Mapped[str | None] = mapped_column(String(120), index=True)
    postal_code: Mapped[str | None] = mapped_column(String(20))
    phone: Mapped[str | None] = mapped_column(String(32))
    email: Mapped[str | None] = mapped_column(String(320))
    website: Mapped[str | None] = mapped_column(Text)

    lead: Mapped["Lead | None"] = relationship(back_populates="restaurant", uselist=False)
    sources: Mapped[list["Source"]] = relationship(back_populates="restaurant")
