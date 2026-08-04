from datetime import date

def calculate_new_streak(last_completed_str, current_streak, max_streak):
    today = date.today()        # 1. Obtenemos la fecha de HOY
    today_str = today.isoformat() # Convertimos la fecha de hoy a texto (ej: "2026-08-03")

    # CASO A: Es la primerísima misión de tu vida (aún no hay fecha guardada)
    if not last_completed_str:
        return 1, max(max_streak, 1), today_str

    # Convertimos la fecha guardada en texto de la BD a un objeto fecha de Python
    last_date = date.fromisoformat(last_completed_str)
    days_passed = (today - last_date).days # 2. Calculamos cuántos días pasaron

    # CASO B: Ya completaste una misión HOY (los días pasados son 0)
    if days_passed == 0:
        return current_streak, max_streak, today_str

    # CASO C: La última fue AYER (pasó exactamente 1 día) -> ¡Sumamos racha!
    elif days_passed == 1:
        new_streak = current_streak + 1
        return new_streak, max(max_streak, new_streak), today_str

    # CASO D: Pasaron 2 días o más -> Se rompió la racha, la reiniciamos a 1
    else:
        return 1, max(max_streak, 1), today_str