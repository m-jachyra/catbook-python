from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def get_list():
    return {"cats": ["Borubar"]}


@router.post("/")
def create_user():
    pass


@router.put("/")
def update_user():
    pass


@router.put("/block")
def lock_user():
    pass