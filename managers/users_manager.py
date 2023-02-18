from passlib.context import CryptContext
from models import users_models
from db import database
from asyncpg import UniqueViolationError
from fastapi import HTTPException
from managers.auth_manager import AuthManager


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class UserManager:
    @staticmethod
    async def register(user_data):
        user_data["password"] = pwd_context.hash(user_data["password"])
        try:
            id_ = await database.execute(
                users_models.users.insert().values(**user_data)
            )
        except UniqueViolationError:
            raise HTTPException(400, "User with this email already exists")
        user_do = await database.fetch_one(
            users_models.users.select().where(users_models.users.c.id == id_)
        )
        return AuthManager.encode_token(user_do)

    @staticmethod
    async def get_user_by_email(email):
        return await database.fetch_all(
            users_models.users.select().where(users_models.users.c.email == email)
        )

    @staticmethod
    async def get_all_users():
        return await database.fetch_all(users_models.users.select())


class AdminManager:
    @staticmethod
    async def register(admin_data):
        admin_data["password"] = pwd_context.hash(admin_data["password"])
        try:
            id_ = await database.execute(
                users_models.admins.insert().values(**admin_data)
            )
        except UniqueViolationError:
            raise HTTPException(400, "Admin with this email already exists")
        user_do = await database.fetch_one(
            users_models.admins.select().where(users_models.admins.c.id == id_)
        )
        return AuthManager.encode_token(user_do)

    @staticmethod
    async def get_admin_by_email(email):
        return await database.fetch_all(
            users_models.admins.select().where(users_models.admins.c.email == email)
        )

    @staticmethod
    async def get_all_admins():
        return await database.fetch_all(users_models.admins.select())


class ModetatorManager:
    @staticmethod
    async def register(moderator_data):
        moderator_data["password"] = pwd_context.hash(moderator_data["password"])
        try:
            id_ = await database.execute(
                users_models.moderators.insert().values(**moderator_data)
            )
        except UniqueViolationError:
            raise HTTPException(400, "Admin with this email already exists")
        user_do = await database.fetch_one(
            users_models.moderators.select().where(users_models.moderators.c.id == id_)
        )
        return AuthManager.encode_token(user_do)

    @staticmethod
    async def get_moderator_by_email(email):
        return await database.fetch_all(
            users_models.moderators.select().where(
                users_models.moderators.c.email == email
            )
        )

    @staticmethod
    async def get_all_moderators():
        return await database.fetch_all(users_models.moderators.select())
