from fastapi import APIRouter

from .controllers import cats_controller, users_controller, default_controller, cat_images_controller, breeds_controller

router = APIRouter()

router.include_router(default_controller.router, tags=["default"])
router.include_router(cats_controller.router, prefix="/cats", tags=["cats"])
router.include_router(users_controller.router, prefix="/users", tags=["users"])
router.include_router(cat_images_controller.router, prefix="/cat_images", tags=["cat_images"])
router.include_router(breeds_controller.router, prefix="/breeds", tags=["breeds"])