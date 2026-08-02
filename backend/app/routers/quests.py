from fastapi import APIRouter, HTTPException, Query
from datetime import date
from typing import Optional
from app.schemas.quest import QuestCreate, QuestResponse
from app.database import get_db_connection # IMPORTAMOS LA CONEXIÓN

router = APIRouter(prefix="/quests", tags=["Quests"])

# --- POST: CREAR MISIÓN ---
@router.post("/", response_model=QuestResponse)
def create_quest(quest: QuestCreate):
    today_str = date.today().isoformat() # Fecha actual dinámica
    
    # 1. Abrimos conexión a la base de datos
    conn = get_db_connection()
    cursor = conn.cursor()

    # 2. Reemplazamos quests_db.append() por un INSERT en SQLite
    cursor.execute(
        "INSERT INTO quests (title, description, experience, state, date) VALUES (?, ?, ?, ?, ?)",
        (quest.title, quest.description, quest.experience, False, today_str)
    )
    conn.commit() # Guardamos los cambios en el archivo .db
    
    # 3. SQLite nos da el ID generado automáticamente (reemplaza a len(quests_db) + 1)
    new_id = cursor.lastrowid
    conn.close() # Cerramos conexión

    # 4. Devolvemos la respuesta tal como lo hacías antes
    return QuestResponse(
        id=new_id,
        state=False,
        date=today_str,
        title=quest.title,
        description=quest.description,
        experience=quest.experience
    )


# --- GET: OBTENER MISIONES (CON FILTRO OPCIONAL) ---
@router.get("/", response_model=list[QuestResponse])
def get_quests(completed: Optional[bool] = Query(None, description="Filtrar por estado: true para completadas, false para pendientes")):
    conn = get_db_connection()
    
    # 1. Si no nos pasan el parámetro completed, traemos todas las misiones
    if completed is None:
        rows = conn.execute("SELECT * FROM quests").fetchall()
    else:
        # 2. Convertimos el booleano (True/False) al entero de SQLite (1/0)
        state_value = 1 if completed else 0
        rows = conn.execute("SELECT * FROM quests WHERE state = ?", (state_value,)).fetchall()
        
    conn.close()
    
    # Convertimos cada fila a diccionario para la respuesta JSON
    return [dict(row) for row in rows]


# --- PATCH: EDITAR MISIÓN ---
@router.patch("/{quest_id}", response_model=QuestResponse)
def update_quest(quest_id: int, quest: QuestCreate):
    conn = get_db_connection()
    cursor = conn.cursor()

    # 1. Buscamos si la misión existe (reemplaza al for loop)
    existing_quest = cursor.execute("SELECT * FROM quests WHERE id = ?", (quest_id,)).fetchone()
    if not existing_quest:
        conn.close()
        raise HTTPException(status_code=404, detail="Quest not found")

    # 2. Actualizamos los campos en la base de datos
    cursor.execute(
        "UPDATE quests SET title = ?, description = ?, experience = ? WHERE id = ?",
        (quest.title, quest.description, quest.experience, quest_id)
    )
    conn.commit()

    # 3. Consultamos la misión ya actualizada para devolverla
    updated = cursor.execute("SELECT * FROM quests WHERE id = ?", (quest_id,)).fetchone()
    conn.close()

    return dict(updated)


# --- PATCH: COMPLETAR MISIÓN Y SUMAR EXP ---
@router.patch("/{quest_id}/complete", response_model=QuestResponse)
def complete_quest(quest_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()

    # 1. Buscamos la misión
    existing_quest = cursor.execute("SELECT * FROM quests WHERE id = ?", (quest_id,)).fetchone()
    if not existing_quest:
        conn.close()
        raise HTTPException(status_code=404, detail="Quest not found")

    # 2. NUEVA VALIDACIÓN: Si ya estaba completada (state == 1 / True), no hacemos nada más
    if existing_quest["state"]:
        conn.close()
        raise HTTPException(status_code=400, detail="La misión ya había sido completada")

    # 3. Marcamos la misión como completada (state = 1)
    cursor.execute("UPDATE quests SET state = 1 WHERE id = ?", (quest_id,))

    # 4. NUEVA LÍNEA CLAVE: Sumamos la experiencia de esta misión al personaje (id=1)
    cursor.execute(
        "UPDATE character SET total_exp = total_exp + ? WHERE id = 1",
        (existing_quest["experience"],)
    )

    conn.commit() # Guardamos ambas actualizaciones juntas en una sola transacción

    # 5. Consultamos la misión actualizada
    updated = cursor.execute("SELECT * FROM quests WHERE id = ?", (quest_id,)).fetchone()
    conn.close()

    return dict(updated)