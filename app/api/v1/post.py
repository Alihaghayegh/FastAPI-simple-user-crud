from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
import sys

sys.path.append("../..")
from app.core.database import get_db
from app.schemas import post
from app.crud import post as post_crud
from app.services.oauth2.oauth2 import get_current_user

router = APIRouter(
    prefix="/posts",
    tags=["posts"]
)


@router.post("", response_model=post.Post)
def create_post(post_create: post.PostCreate, db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    return post_crud.create_post(db=db, post=post_create)


@router.get("", response_model=List[post.Post])
def get_posts():
    pass


@router.get("")
def get_post_by_id():
    pass


@router.put("/update")
def update_post():
    pass


@router.delete("")
def delete_post():
    pass
