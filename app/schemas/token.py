from pydantic import BaseModel


class Login(BaseModel):
    email: str
    password: str

    class Config:
        orm_mode = True


class AccessToken(BaseModel):
    access_token: str
    token_type: str 