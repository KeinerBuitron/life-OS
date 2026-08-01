from fastapi import FastAPI
from app.routers import character, quests

app = FastAPI(title="Life-OS API")
app.include_router(character.router)
app.include_router(quests.router)

@app.get("/")
def read_root():
    return {"message": "Bienvenido a Life-OS API!"}
