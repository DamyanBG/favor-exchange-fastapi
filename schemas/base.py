from pydantic import BaseModel


class UserBase(BaseModel):
    email: str


class FavorBase(BaseModel):
    title: str
    text: str