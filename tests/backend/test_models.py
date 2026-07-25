from app.db.base import Base
import app.models  # noqa: F401


def test_mvp_metadata_contains_only_authorized_tables() -> None:
    assert set(Base.metadata.tables) == {
        "users",
        "restaurants",
        "leads",
        "interactions",
        "sources",
    }


def test_mvp_relations_are_declared() -> None:
    leads = Base.metadata.tables["leads"]
    interactions = Base.metadata.tables["interactions"]
    sources = Base.metadata.tables["sources"]

    assert {foreign_key.target_fullname for foreign_key in leads.foreign_keys} == {
        "restaurants.id",
        "users.id",
    }
    assert {foreign_key.target_fullname for foreign_key in interactions.foreign_keys} == {"leads.id"}
    assert {foreign_key.target_fullname for foreign_key in sources.foreign_keys} == {"restaurants.id"}
