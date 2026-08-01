XP_TOTAL = 450
XP_FOR_LEVEL = 200
XP_TOTAL = 450
def level_player(xp: int):
    level = 1 + xp // XP_FOR_LEVEL 
    return level

def exp_residue(xp: int):
    residue = xp % XP_FOR_LEVEL
    return residue
