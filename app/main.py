from fastapi import FastAPI
import sys


sys.path.append("..")
from app.api.v1 import users, login
from app.core.database import Base, engine


Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def greet():
    return {"message": "hello world"}


app.include_router(login.router)
app.include_router(users.router)
