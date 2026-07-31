XP_FOR_LEVEL = 200
def level_player(xp: int):
    level = 1 + xp // XP_FOR_LEVEL 
    return level

def exp_residue(xp: int):
    residue = xp % XP_FOR_LEVEL
    return residue

message = "Felicidades, nuevo nivel alcanzado: "
print(message, level_player(600))
print(f'Exp restante: {exp_residue(430)}->200')