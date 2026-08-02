# Backlog
- [ ] Dificultad o Tipo: Misiones Diarias (Dailies), Hábitos o Misiones Principales (Main Quests).

- [ ] Rachas (Streaks): Si el personaje completa al menos una misión al día, aumenta su racha.

- [ ] Historial/Registro: Guardar cuándo fue la última vez que completó una misión.

- [ ] Configurar CORS (Cross-Origin Resource Sharing) en FastAPI para permitir que un frontend se conecte a tu API sin bloqueos de seguridad.

- [ ] Diseñar logo

- [ ] Login

- [ ] Registro

- [ ] Dashboard

- [ ] Sistema XP

- [ ] Base de datos

- [ ] Crear Avatar

- [ ] Estadísticas

      # En progreso

- [ ] Documento del proyecto

# Finalizado

- [x] Filtros en el GET: Poder consultar solo misiones pendientes (state = 0) o completadas (state = 1).

- [x] Crear app/routers/quests.py con los endpoints POST para crear y completar misiones.

- [x] Incluir el nuevo router en main.py.

- [x] Probar en [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) que puedes crear una misión y simular su completado.

- [x] Crear app/schemas/quest.py con las clases de Pydantic.

- [x] Crear repositorio

- [x] Definir visión

- [x] Elegir nombre

# Finalizado
- [x] Crear app/routers/quests.py con los endpoints POST para crear y completar misiones.
- [x] Implementar endpoint GET /quests/ para listar todas las misiones en memoria.
- [x] Implementar endpoint PATCH /quests/{quest_id}/complete para marcar misiones como completadas.
- [x] Incluir el nuevo router en main.py.
- [x] Probar en http://127.0.0 que puedes crear una misión, ver el listado y simular su completado.
- [x] Crear app/schemas/quest.py con las clases de Pydantic.
- [x] Crear repositorio
- [x] Definir visión
- [x] Elegir nombre

   ┌─────────────────────────────────────────────────────────┐
   │                       LIFE OS API                       │
   └─────────────────────────────────────────────────────────┘
                                │
        ┌───────────────────────┴───────────────────────┐
        ▼                                               ▼
  [ /character ]                                  [ /quests ]
  • GET /profile                                  • POST /
    (Cálculo de XP y Nivel)                         (Creación de misiones)
                                                  • GET /
                                                    (Listar misiones)
                                                  • PATCH /{quest_id}/complete
                                                    (Completar misión)
