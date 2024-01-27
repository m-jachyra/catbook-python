from fastapi import APIRouter

from .controllers import cats_controller, users_controller, default_controller, auth_controller

router = APIRouter()

router.include_router(default_controller.router, tags=["default"])
# router.include_router(auth_controller.router, tags=["/auth"])
router.include_router(cats_controller.router, prefix="/cats", tags=["cats"])
router.include_router(users_controller.router, prefix="/users", tags=["users"])
