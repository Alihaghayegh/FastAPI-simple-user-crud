# FastAPI Simple User CRUD API

* This App serves the CRUD API for users written in FastAPI.
* It simply recieves a post request for adding user and saves it to database.
* The default config it on PostgreSQL but feel free to uncomment the SQLite config in ***core/dabase.py***.
```python
# SQLALCHEMY_DATABASE_URL = "sqlite:///./users.db"
SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
# )
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
```
* Create your **.env** file and put your main config in it.

* To start the App run the following commands in your terminal:

for installing the dependencies:
```bash
$ pip3 install -r requirements.txt
```
for starting the App:
```bash
$ uvicorn main:app --reload
```
