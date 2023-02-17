from fastapi import APIRouter, Depends
from managers.users_manager import UserManager

from schemas.reguest.user import UserRegisterIn

router = APIRouter(tags=["Users"])



@router.get(
    "/users/",
    dependencies=[],
    # response_model=List[UserOut],
)
async def get_users():
    all_users = await UserManager.get_all_users()
    return all_users 


@router.post(
    "/users/",
    status_code=201,
)
async def create_user(user_data: UserRegisterIn):
    print("wliza")
    token = await UserManager.register(user_data.dict())
    return {"token": token}

