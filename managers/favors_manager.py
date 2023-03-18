from db import database
from models import favors_model

class FavorManager:
    @staticmethod
    async def create_favor(favor_data, user):
        favor_data["user_id"] = user["id"]
        id_ = await database.execute(
            favors_model.favors.insert().values(favor_data)
        )
        new_favor = await database.fetch_one(favors_model.favors.select().where(favors_model.favors.c.id == id_))
        return new_favor
    
    @staticmethod
    async def select_favors_by_user(user):
        q = favors_model.favors.select()
        q = q.where(favors_model.favors.c.user_id == user["id"])
        user_favors = await database.fetch_all(q)
        return user_favors
    
    @staticmethod
    async def select_all_favors():
        q = favors_model.favors.select()
        all_favors = await database.fetch_all(q)
        return all_favors
