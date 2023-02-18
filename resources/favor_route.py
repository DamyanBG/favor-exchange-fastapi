from fastapi import APIRouter, Depends
from managers.favors_manager import FavorManager
from starlette.requests import Request

from schemas.reguest.favor import FavorCreate
from managers.auth_manager import oauth2_scheme

router = APIRouter(tags=["Favors"])

@router.get(
    "/user_favors/",
    dependencies=[Depends(oauth2_scheme)],
)
async def get_user_favors(request: Request):
    user = request.state.user
    return await FavorManager.select_favors_by_user(user)