from contextlib import asynccontextmanager
from app.database import init_db
from fastapi import FastAPI
from app.routers import character, quests
from fastapi.middleware.cors import CORSMiddleware

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Se ejecuta al arrancar el servidor
    init_db()
    yield

app = FastAPI(lifespan=lifespan, title="Life-OS API")
app.include_router(character.router)
app.include_router(quests.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Bienvenido a Life-OS API!"}
