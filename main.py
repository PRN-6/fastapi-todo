from fastapi import FastAPI
from routes.task import router
from database.session import engine , Base
from models.task import Task

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router)

