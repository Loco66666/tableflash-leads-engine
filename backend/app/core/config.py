from functools import cached_property

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    environment: str = "development"
    api_v1_prefix: str = "/api/v1"
    database_url: str = "postgresql+psycopg://tfle:tfle@localhost:5432/tfle"
    cors_origins: str = "http://localhost:5173"
    jwt_secret_key: str = "development-only-change-me-use-a-long-random-secret"
    jwt_access_token_expire_minutes: int = 480

    @cached_property
    def cors_origin_list(self) -> list[str]:
        return [origin.strip() for origin in self.cors_origins.split(",") if origin.strip()]


settings = Settings(
    _env_prefix="TFLE_",
)
