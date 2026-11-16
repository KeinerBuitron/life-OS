# Life OS

Aplicación móvil de productividad gamificada inspirada en sistemas RPG. Convierte tus tareas diarias en **misiones (quests)** que otorgan **experiencia (EXP)**, suben el nivel de tu personaje y mantienen tus **rachas diarias**.

---

## Características implementadas

- **Gestión de misiones (`Quests`)**: creación, listado con filtro por estado (pendientes/completadas), edición y marcado como completadas.
- **Sistema de experiencia y niveles**: al completar una misión se suma su EXP al personaje y se calcula el nivel actual (`200 EXP` por nivel) y el progreso restante.
- **Sistema de rachas (`Streaks`)**: cálculo automático de racha actual y racha máxima según la fecha de la última misión completada.
- **Persistencia local en servidor**: base de datos SQLite inicializada automáticamente al arrancar la API.
- **Cliente Android nativo**: consumo de la API REST mediante Retrofit, visualización del perfil del personaje y listado interactivo de misiones con `RecyclerView`.

---

## Arquitectura y Stack Tecnológico

```text
life-OS/
├── backend/                 # API REST con FastAPI + SQLite
│   ├── main.py              # Punto de entrada y configuración CORS
│   └── app/
│       ├── database.py      # Conexión e inicialización de tablas SQLite
│       ├── routers/         # Endpoints (/quests, /character)
│       ├── schemas/         # Validación y serialización con Pydantic
│       └── services/        # Lógica de niveles, EXP y rachas
├── android/                 # App móvil nativa en Java
│   └── app/src/main/
│       ├── java/com/tu_nombre/lifeos/
│       │   ├── MainActivity.java
│       │   ├── adapters/    # QuestAdapter (RecyclerView)
│       │   ├── models/      # DTOs de respuesta
│       │   └── network/     # RetrofitClient y ApiService
│       └── res/layout/      # Vistas XML
└── docs/
```

| Capa | Tecnología |
| --- | --- |
| **Backend** | Python 3.12+, FastAPI, Uvicorn, Pydantic |
| **Base de datos** | SQLite3 |
| **App móvil** | Android SDK, Java 11, XML Views, Material Components |
| **Red / Cliente HTTP** | Retrofit 2 + Gson |

---

## Endpoints de la API

| Método | Ruta | Descripción |
| --- | --- | --- |
| `GET` | `/` | Mensaje de bienvenida / estado de la API |
| `GET` | `/character/Profile` | Perfil del personaje (nivel, EXP total, residuo y rachas) |
| `GET` | `/quests/` | Lista todas las misiones (opcional `?completed=true\|false`) |
| `POST` | `/quests/` | Crea una nueva misión |
| `PATCH` | `/quests/{quest_id}` | Edita una misión existente |
| `PATCH` | `/quests/{quest_id}/complete` | Completa una misión, suma EXP y actualiza la racha |

---

## Cómo ejecutar el proyecto en local

### 1. Backend (FastAPI)

1. Crea y activa un entorno virtual dentro de `backend/` o en la raíz e instala las dependencias:
   ```bash
   python -m venv .venv
   # En Windows:
   .venv\Scripts\activate
   pip install fastapi uvicorn
   ```
2. Entra a la carpeta `backend/` (necesario para que SQLite resuelva `life_os.db` correctamente) y levanta el servidor:
   ```bash
   cd backend
   uvicorn main:app --reload
   ```
3. Documentación interactiva disponible en: `http://127.0.0.1:8000/docs`

### 2. App Android

1. Abre la carpeta `android/` en **Android Studio**.
2. Asegúrate de tener el backend corriendo en el puerto `8000`.
3. Ejecuta la app en un emulador (usa `http://10.0.2.2:8000/` configurado en `RetrofitClient.java`). Si pruebas en un dispositivo físico, reemplaza la URL por la IP local de tu PC.

---

## Roadmap

- Autenticación de usuarios (registro y login)
- Clasificación de misiones (diarias, hábitos, misiones principales)
- Personalización de avatar y estadísticas históricas

---

## Colaboradores

- **Keiner Buitrón**
- **Mauricio Florez**
