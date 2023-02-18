from typing import List
from fastapi import APIRouter, Depends
from starlette.requests import Request

from managers.favors_manager import FavorManager
from schemas.reguest.favor import FavorCreate
from schemas.response.favor import FavorOut
from managers.auth_manager import oauth2_scheme

router = APIRouter(tags=["Favors"])

@router.get(
    "/user_favors/",
    dependencies=[Depends(oauth2_scheme)],
    response_model=List[FavorOut]
)
async def get_user_favors(request: Request):
    user = request.state.user
    user_favors = await FavorManager.select_favors_by_user(user)
    return user_favors

@router.post(
    "/user_favors/",
    dependencies=[Depends(oauth2_scheme),],
)
async def create_favor(request: Request, favor: FavorCreate):
    user = request.state.user
    new_favor = await FavorManager.create_favor(favor.dict(), user)
    return new_favor
