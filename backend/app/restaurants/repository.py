from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.restaurant import Restaurant
from app.restaurants.schemas import RestaurantCreate


class RestaurantRepository:
    def __init__(self, session: Session) -> None:
        self.session = session

    def create(self, payload: RestaurantCreate) -> Restaurant:
        restaurant = Restaurant(**payload.model_dump())
        self.session.add(restaurant)
        self.session.commit()
        self.session.refresh(restaurant)
        return restaurant

    def list(self) -> list[Restaurant]:
        statement = select(Restaurant).order_by(Restaurant.created_at.desc())
        return list(self.session.scalars(statement))
