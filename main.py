from fastapi import FastAPI
from routes.task import router

app = FastAPI()

app.include_router(router)