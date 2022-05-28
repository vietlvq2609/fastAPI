# from typing import Optional

from pydantic import BaseModel

class UserInCreate(BaseModel):
    name: str
    password: str
    phone: str

class UserInResponse(BaseModel):
    id: int
    name: str
    phone: str

    class Config:
        orm_mode = True

class UserInLogin(BaseModel):
    phone: str
    password: str