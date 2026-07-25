from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.health import router as health_router
from app.core.config import settings
from app.restaurants.router import router as restaurants_router

app = FastAPI(title="TFLE API", version="0.1.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origin_list,
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)
app.include_router(health_router, prefix=settings.api_v1_prefix)
app.include_router(restaurants_router, prefix=settings.api_v1_prefix)
