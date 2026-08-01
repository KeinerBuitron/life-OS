# Backlog

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
- [x] Crear app/routers/quests.py con los endpoints POST para crear y completar     misiones.

- [x] Incluir el nuevo router en main.py.

- [x] Probar en [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) que puedes crear una misión y simular su completado.

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