from fastapi import APIRouter, Depends
from managers.users_manager import UserManager, AdminManager, ModetatorManager

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


@router.get(
    "/admins/",
    dependencies=[],
    # response_model=List[UserOut],
)
async def get_admins():
    all_admins = await AdminManager.get_all_admins()
    return all_admins


@router.post(
    "/admins/",
    status_code=201,
)
async def create_admin(admin_data: UserRegisterIn):
    print("wliza")
    token = await AdminManager.register(admin_data.dict())
    return {"token": token}


@router.get(
    "/moderators/",
    dependencies=[],
    # response_model=List[UserOut],
)
async def get_moderators():
    all_admins = await ModetatorManager.get_all_moderators()
    return all_admins


@router.post(
    "/moderators/",
    status_code=201,
)
async def create_user(moderator_data: UserRegisterIn):
    print("wliza")
    token = await ModetatorManager.register(moderator_data.dict())
    return {"token": token}
