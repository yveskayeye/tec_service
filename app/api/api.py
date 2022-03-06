from fastapi import APIRouter

from api.endpoints import login, users, respond, admin

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(admin.router, tags=["admin"])
api_router.include_router(respond.router, tags=["respond"])
api_router.include_router(users.router, tags=["users"])