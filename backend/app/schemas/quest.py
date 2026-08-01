from pydantic import BaseModel #Para validacion de datos

# 1. Campos compartidos
class QuestBase(BaseModel):
    title: str
    description: str
    experience: int

# 2. Lo que recibe el POST para crear
class QuestCreate(QuestBase):
    pass

# 3. Lo que devuelve la API (agrega los datos del sistema)
class QuestResponse(QuestBase):
    id: int
    state: bool
    date: str
