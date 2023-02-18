from fastapi import APIRouter
from resources import user_route, favor_route

api_router = APIRouter()
api_router.include_router(user_route.router)
api_router.include_router(favor_route.router)
