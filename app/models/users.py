from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship
from .post import Post
import sys


sys.path.append("../")
from app.core.database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    date = Column(Date)
    post = relationship('Post', back_populates='owner')
