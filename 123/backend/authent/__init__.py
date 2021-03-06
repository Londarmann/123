from fastapi import APIRouter

from mango.views import router as user_router

router = APIRouter()
router.include_router(user_router)