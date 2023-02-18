from db import database
from models import favors_model

class FavorManager:
    @staticmethod
    async def create_favor(favor_data):
        id_ = await database.execute(
            favors_model.insert().values(**favor_data)
        )
        new_favor = favors_model.select().where(favors_model.c.id == id_)
        return new_favor
    
    @staticmethod
    async def select_favors_by_user(user):
        q = favors_model.select()
        q = q.where(favors_model.c.id == user["id"])
        user_favors = await database.fetch_all(q)
        return user_favors
