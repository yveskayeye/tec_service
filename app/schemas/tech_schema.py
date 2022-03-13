from datetime import datetime
from pydantic import BaseModel


class TechInfo(BaseModel):
   pass


class TechCreate(BaseModel):
    password: str
    is_superuser: bool
    email: str
    name: str
    title: str
    jobs_responded: int

    class Config:
        orm_mode = True


class TechUpdate(BaseModel):
    is_superuser: bool

    class Config:
        orm_mode = True
