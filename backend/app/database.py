import sqlite3

DATABASE_NAME = "life_os.db"

def get_db_connection():
    conn = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = sqlite3.Row  # Permite acceder a las columnas por nombre como un diccionario
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Tabla de Personaje
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS character (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            total_exp INTEGER NOT NULL DEFAULT 0,
            current_streak INTEGER NOT NULL DEFAULT 0,
            max_streak INTEGER NOT NULL DEFAULT 0,
            last_completed_date TEXT 
        );  
    """)

    # Tabla de Misiones
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS quests (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            experience INTEGER NOT NULL,
            state BOOLEAN NOT NULL DEFAULT 0,
            date TEXT NOT NULL
        );
    """)

    # Crear personaje inicial si la tabla está vacía
    cursor.execute("SELECT COUNT(*) FROM character")
    if cursor.fetchone()[0] == 0:
        #Pasamos los valores iniciales para las rachas (0, 0, None)
        cursor.execute("""
            INSERT OR IGNORE INTO character (id, username, total_exp, current_streak, max_streak, last_completed_date)
            VALUES (1, 'Hero', 0, 0, 0, NULL)
        """)
        
    conn.commit()
    conn.close()