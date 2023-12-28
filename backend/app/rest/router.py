from fastapi import APIRouter

from controllers import cats_controller, users_controller

router = APIRouter()

router.include_router(cats_controller.router, tags=["cats"])
router.include_router(users_controller.router, tags=["users"])
