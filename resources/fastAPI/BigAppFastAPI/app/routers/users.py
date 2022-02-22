from fastapi import APIRouter

router =  APIRouter()

@router.get("/users/", tags=["users"])
async def read_users():
    return [ {"username": "shreyas"}, {"username": "Samaya"}]

@router.get("/users/me", tags=["users"])
async def read_user_me():
    return { "username" : "shreyasUser"}


@router.get("/users/{username}", tags=["users"])
async def read_user(username: str):
    return {"username" : username}