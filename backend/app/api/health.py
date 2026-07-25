from fastapi import APIRouter, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.db.session import get_db

router = APIRouter(tags=["system"])


@router.get("/health")
def health_check(session: Session = Depends(get_db)) -> dict[str, str]:
    """Return the API and PostgreSQL liveness state."""
    session.execute(text("SELECT 1"))
    return {"status": "ok", "database": "ok"}
