from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
import sys

sys.path.append("../..")
from app.core.database import get_db
from app.schemas import users
from app.crud import users as user_crud
from app.services.oauth2.oauth2 import get_current_user

router = APIRouter(
    prefix="/users",
    tags=['users']
)


@router.post("", response_model=users.User)
def create_user(user: users.UserCreate, db: Session = Depends(get_db)):
    db_user = user_crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return user_crud.create_user(db=db, user=user)


@router.get("", response_model=List[users.User])
def read_users(current_page: int = 1, page_size: int = 20, db: Session = Depends(get_db), get_current_user: users.User = Depends(get_current_user)):
    users = user_crud.get_users(db, current_page=current_page, page_size=page_size)
    return users


@router.get("{user_id}", response_model=users.User)
def read_user(user_id: int, db: Session = Depends(get_db), get_current_user: users.User = Depends(get_current_user)):
    db_user = user_crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
