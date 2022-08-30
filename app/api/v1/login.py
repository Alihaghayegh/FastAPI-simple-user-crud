from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
import sys

sys.path.append("../..")
from app.core.database import get_db
from app.models import users
from app.services.hashing.hashing import Hasher
from app.services.tokenCreate import tokenCreate

router = APIRouter(
    prefix="/login",
    tags=['login']
)


@router.post("")
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db), password: str = None):
    user = db.query(users.User).filter(
        users.User.email == request.username).first()
    if not user and Hasher.verify_password(password, users.User.hashed_password):
        return False

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="invalid Credentials")
    access_token = tokenCreate.create_access_token(
        data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}
