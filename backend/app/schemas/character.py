from pydantic import BaseModel #Para validacion de datos

class CharacterResponse(BaseModel):
    username: str
    level: int
    total_exp: int
    exp_residue: int
    next_level_exp: int
