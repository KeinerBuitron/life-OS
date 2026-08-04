from fastapi import APIRouter, HTTPException
from app.schemas.character import CharacterResponse
from app.services.gamification import level_player, exp_residue, XP_FOR_LEVEL
from app.database import get_db_connection

router = APIRouter(prefix="/character", tags=["Character"])

@router.get("/Profile", response_model=CharacterResponse)
def get_character_profile():
    # 1. En lugar de total_exp = 430, lo leemos de la base de datos
    conn = get_db_connection()
    character = conn.execute("SELECT * FROM character WHERE id = 1").fetchone()
    conn.close()

    # Si por alguna razón la tabla está vacía, lanzamos un error 404
    if not character:
        raise HTTPException(status_code=404, detail="Personaje no encontrado en la base de datos")

    # 3. Extraemos los valores guardados en SQLite
    username = character["username"]
    total_exp = character["total_exp"]
    current_streak = character["current_streak"]
    max_streak = character["max_streak"]
    
    return CharacterResponse(
        username=username,
        level=level_player(total_exp), # Tu función de gamificación
        total_exp=total_exp,           # La XP real leída de SQLite
        exp_residue=exp_residue(total_exp), # Tu función de residuo
        next_level_exp=XP_FOR_LEVEL,
        current_streak=current_streak,
        max_streak=max_streak
    )