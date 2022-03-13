from pydantic import BaseSettings

class Settings(BaseSettings):
    SQL_DATABASE_URI: str 

    class Config:
        env_file = ".env"



settings = Settings()