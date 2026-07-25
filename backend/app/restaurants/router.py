from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.auth.dependencies import get_current_user
from app.db.session import get_db
from app.models.user import User
from app.restaurants.schemas import RestaurantCreate, RestaurantRead
from app.restaurants.service import RestaurantService

router = APIRouter(prefix="/restaurants", tags=["restaurants"])


@router.post("", response_model=RestaurantRead, status_code=status.HTTP_201_CREATED)
def create_restaurant(
    payload: RestaurantCreate,
    session: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> RestaurantRead:
    return RestaurantService(session).create(payload)


@router.get("", response_model=list[RestaurantRead])
def list_restaurants(
    session: Session = Depends(get_db), current_user: User = Depends(get_current_user)
) -> list[RestaurantRead]:
    return RestaurantService(session).list()
