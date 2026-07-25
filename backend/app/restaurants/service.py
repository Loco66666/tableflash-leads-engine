from sqlalchemy.orm import Session

from app.models.restaurant import Restaurant
from app.restaurants.repository import RestaurantRepository
from app.restaurants.schemas import RestaurantCreate


class RestaurantService:
    def __init__(self, session: Session) -> None:
        self.repository = RestaurantRepository(session)

    def create(self, payload: RestaurantCreate) -> Restaurant:
        return self.repository.create(payload)

    def list(self) -> list[Restaurant]:
        return self.repository.list()
