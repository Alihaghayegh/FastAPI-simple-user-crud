import os
from dotenv import load_dotenv
from pydantic import BaseSettings

from pathlib import Path
env_path = Path('../') / '.env'
load_dotenv(dotenv_path=env_path)


class Settings(BaseSettings):
    PROJECT_NAME: str = "FastAPI-App"
    PROJECT_VERSION: str = "1.0.0"

    JWT_SECRET_KEY: str = os.getenv("SECRET_KEY")
    ALGORRITHM: str = os.getenv("ALGORITHM")
    POSTGRES_USER: str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_SERVER: str = os.getenv("POSTGRES_SERVER")
    POSTGRES_PORT: str = os.getenv("POSTGRES_PORT")
    POSTGRES_DATABASE: str = os.getenv("POSTGRES_DATABASE")
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DATABASE}"


settings = Settings()
