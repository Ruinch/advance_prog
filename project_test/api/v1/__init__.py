from fastapi import APIRouter

from api.v1.auth import router as auth_router
from api.v1.users import router as users_router

router = APIRouter()

router.include_router(auth_router, prefix="/auth", tags=["Auth"])
router.include_router(users_router, prefix="/users", tags=["Users"])
