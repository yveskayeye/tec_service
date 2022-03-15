from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.config import settings
from app.schemas import tech_schema
from .. import depends
from app.models import tech
from app.crud import tech


router = APIRouter()

@router.get('/{tech_id}', response_model = tech_schema.TechBase)
def login(
    tech_id: int,
    current_user: tech.Tech = Depends(depends.get_current_active_user),
    db: Session = Depends(depends.get_db),
)-> Any:
    user = tech.user.get(db, id=tech_id)
    if user == current_user:
        return user
    if not tech.user.is_superuser(current_user):
        raise HTTPException(
            status_code=400, detail="The user doesn't have enough privileges"
        )
    return user


@router.get("/me", response_model=tech_schema.TechBase)
def read_user_me(
    db: Session = Depends(depends.get_db),
    current_user: tech.Tech = Depends(depends.get_current_active_user),
) -> Any:
    """
    Get current user.
    """
    return current_user


@router.get("/", response_model=List[tech_schema.TechBase])
def read_users(
    db: Session = Depends(depends.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: tech.Tech = Depends(depends.get_current_active_superuser),
) -> Any:
    """
    Retrieve users.
    """
    users = tech.user.get_multi(db, skip=skip, limit=limit)
    return users


@router.post("/", response_model=tech_schema.TechCreatedResponse)
def create_user(
    *,
    db: Session = Depends(depends.get_db),
    user_in: tech_schema.TechCreate,
    current_user: tech.Tech = Depends(depends.get_current_active_superuser),
) -> Any:
    """
    Create new user.
    """
    user = tech.user.get_by_email(db, email=user_in.email)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this username already exists in the system.",
        )
    user = tech.user.create(db, obj_in=user_in)
    # if settings.EMAILS_ENABLED and user_in.email:
    #     send_new_account_email(
    #         email_to=user_in.email, username=user_in.email, password=user_in.password
    #     )
    return user