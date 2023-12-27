from fastapi import APIRouter

router = APIRouter()

@router.get('/')
def get_list():
    return {"cats": ["Borubar"]}
