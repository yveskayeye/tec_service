from typing import Any

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from ...schemas import token
from .. import depends


router = APIRouter()

router.post('/login', response_model=token.AccessToken)
def login( db: Session = Depends(depends.get_db), form_data: OAuth2PasswordRequestForm = Depends()
)-> Any:
    pass