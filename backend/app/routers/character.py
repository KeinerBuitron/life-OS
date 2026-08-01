from fastapi import APIRouter
from app.schemas.character import CharacterResponse
from app.services.gamification import level_player, exp_residue, XP_FOR_LEVEL, XP_TOTAL

router = APIRouter(prefix="/character", tags=["Character"])

@router.get("/Profile", response_model=CharacterResponse)
def get_character_profile():
    total_exp = 430

    return CharacterResponse(
        username="Random",
        level=level_player(total_exp),
        total_exp=total_exp,
        exp_residue=exp_residue(total_exp),
        next_level_exp=XP_FOR_LEVEL
    )
