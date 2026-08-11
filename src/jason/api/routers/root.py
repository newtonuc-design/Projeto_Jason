from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def root():
    return {
        "app": "Jason Barber",
        "status": "online"
    }
