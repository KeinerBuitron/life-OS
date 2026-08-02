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
            total_exp INTEGER NOT NULL DEFAULT 0
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
        cursor.execute("INSERT INTO character (username, total_exp) VALUES (?, ?)", ("Keiner", 0))

    conn.commit()
    conn.close()