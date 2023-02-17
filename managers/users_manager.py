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
            id_ = await database.execute(users_models.users.insert().values(**user_data))
        except UniqueViolationError:
            raise HTTPException(400, "User with this email already exists")
        user_do = await database.fetch_one(users_models.users.select().where(users_models.users.c.id == id_))
        return AuthManager.encode_token(user_do)
    
    @staticmethod
    async def get_user_by_email(email):
        return await database.fetch_all(users_models.users.select().where(users_models.users.c.email == email))
    
    @staticmethod
    async def get_all_users():
        return await database.fetch_all(users_models.user.select())