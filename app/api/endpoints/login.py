from typing import Any
from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.schemas import token
from .. import depends
from app.crud import tech
from app.core import security
from app.core.config import settings


router = APIRouter()

router.post('/login/access-token', response_model=token.AccessToken)
def login( db: Session = Depends(depends.get_db), form_data: OAuth2PasswordRequestForm = Depends()
)-> Any:
    user = tech.user.authenticate(
        db, email=form_data.username, password=form_data.password
    )
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
        
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    return {
        "access_token": security.create_access_token(
            user.id, expires_delta=access_token_expires
        ),
        "token_type": "bearer",
    }
