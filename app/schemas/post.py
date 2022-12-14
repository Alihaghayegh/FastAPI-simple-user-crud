from pydantic import BaseModel


class PostBase(BaseModel):
    title: str
    description: str


class Post(PostBase):
    id: int

    class Config:
        orm_mode = True


class PostUpdate(PostBase):
    pass


class PostCreate(PostBase):
    pass
