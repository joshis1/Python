from fastapi import APIRouter as APIRouter

router = APIRouter()

@router.get("/")
async def get_company_name():
    return {"company_name": "Example Company"}


@router.get("/employees")
async def number_of_employees():
    return 180