# Life OS - Arquitectura del Sistema

## Stack Tecnológico

### Android Client (Mobile)
- **Lenguaje:** Kotlin
- **UI:** Jetpack Compose (Material 3)
- **Arquitectura:** Clean Architecture + MVVM
- **Inyección de Dependencias:** Hilt
- **Navegación:** Jetpack Navigation Compose
- **Conectividad / Red:** Retrofit + OkHttp

### Backend API
- **Framework:** FastAPI (Python)
- **ORM:** SQLAlchemy (Async)
- **Migraciones:** Alembic
- **Autenticación:** OAuth2 / JWT (JSON Web Tokens)
- **Documentación API:** OpenAPI / Swagger UI

### Base de Datos e Infraestructura
- **Base de Datos Relacional:** PostgreSQL
- **Notificaciones Push:** Firebase Cloud Messaging (FCM)
- **Contenedores & Proxy:** Docker, Docker Compose, Nginx
