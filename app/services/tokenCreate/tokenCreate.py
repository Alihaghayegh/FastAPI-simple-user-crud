from datetime import datetime, timedelta
from typing import Union
from jose import JWTError, jwt
from app.schemas import token as tokendata


# import os
# from dotenv import load_dotenv
# from pathlib import Path

# env_path = Path('.') / '.env'
# load_dotenv(dotenv_path=env_path)

# SECRET_KEY: str = os.getenv(SECRET_KEY)
# ALGORITHM: str = os.getenv(ALGORITHM)
# ACCESS_TOKEN_EXPIRE_MINUTES:str = os.getenv(ACCESS_TOKEN_EXPIRE_MINUTES)

SECRET_KEY = "4cde175c049eca588a318c5743eeb4f370698abc8a37ed825483b20b04828f10"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY,
                             algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = tokendata.TokenData(username=username)
    except JWTError:
        raise credentials_exception
