from fastapi import HTTPException, status
from sqlalchemy.orm import Session
import datetime
import sys

sys.path.append("../")
from app.models import post as post_model
from app.schemas import post as post_schema


def get_post_by_id(db: Session, post_id: int):
    return db.query(post_model.Post).filter(post_model.Post.id == post_id).first()


def get_post_by_title(db: Session, post_title: str):
    return db.query(post_model.Post).filter(post_model.Post.title == post_title).first()


def get_all_posts(db: Session, current_page: int = 0, page_size: int = 20):
    if page_size <= 0:
        raise HTTPException(status_code=400, detail="Invalid page size")
    if current_page <= 0:
        raise HTTPException(status_code=404, detail="Page not found")
    return db.query(post_model.Post).offset((current_page - 1) * page_size).limit(page_size).all()


def create_post(db: Session, post: post_schema.Post):
    db_post = post_model.Post(
        title=post.title, description=post.description, date_posted=datetime.date.today()
    )
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    raise HTTPException(status_code=status.HTTP_201_CREATED, detail="post successfully added")
    return db_user


def update_post(db: Session, post_update: post_schema.PostUpdate, post_id: int):
    query = post_model.Post.filter(post_model.Post.id == post_id)
    if not db.execute(query.first()):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Post not found"
        )
    query.update(post_update.__dict__)
    db.commit()
    message = {"message": "Post successfully updated"}
    return message


def delete_post(
        db: Session, post_id: int
):
    query = post_model.Post.filter(post_id == post_model.Post.id)
    if not db.execute(query.first()):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Post with not found"
        )
    query.delete()
    db.commit()
    message = {"message": "Post successfully deleted"}
    return message
