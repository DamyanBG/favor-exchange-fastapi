from schemas.base import FavorBase


class FavorOut(FavorBase):
    id: int
    user_id: int
