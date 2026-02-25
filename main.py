from fastapi import FastAPI
from .database import engine
from . import models
from .routers import obras

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Sistema Controle de Obras")

app.include_router(obras.router)
