from fastapi import HTTPException, status
from sqlalchemy.orm import Session
import datetime
import sys
sys.path.append("../")
from app.models import users as user_model
from app.schemas import users as user_schema
from app.services.hashing.hashing import Hasher


def get_user(db: Session, user_id: int):
    return db.query(user_model.User).filter(user_model.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(user_model.User).filter(user_model.User.email == email).first()


def get_users(db: Session, current_page: int = 0, page_size: int = 20):
    if page_size <= 0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid page size")
    if current_page <= 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Page not found")
    return db.query(user_model.User).offset((current_page - 1) * page_size).limit(page_size).all()


def create_user(db: Session, user: user_schema.UserCreate):
    CryptHandler = Hasher.get_password_hash(user.password)
    db_user = user_model.User(
        email=user.email, hashed_password=CryptHandler, date=datetime.date.today())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    raise HTTPException(status_code=status.HTTP_201_CREATED, detail="User created successfully")
    return db_user
