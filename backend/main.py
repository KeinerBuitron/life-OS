from contextlib import asynccontextmanager
from app.database import init_db
from fastapi import FastAPI
from app.routers import character, quests

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Se ejecuta al arrancar el servidor
    init_db()
    yield

app = FastAPI(title="Life-OS API")
app.include_router(character.router)
app.include_router(quests.router)

@app.get("/")
def read_root():
    return {"message": "Bienvenido a Life-OS API!"}
