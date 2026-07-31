from app.services.gamification import level_player, exp_residue, XP_FOR_LEVEL, XP_TOTAL
name = "Player1"
atributes = {
    "username": name,
    "level": level_player(XP_TOTAL),
    "exp_residue" : exp_residue(XP_TOTAL),
    "next_level_exp": XP_FOR_LEVEL,
    "total_exp" : XP_TOTAL
}

print(atributes)