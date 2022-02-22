from fastapi import APIRouter as APIRouter
router = APIRouter()

@router.post("/")
async def update_admin():
    return {"message": "Admin getting notify"}