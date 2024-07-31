### Lead Management API

Esta es una API RESTful para la gestión de leads, utilizando FastAPI y PostgreSQL. La API permite registrar leads con múltiples materias y consultar la información cargada.

### Tecnologías Utilizadas

-FastAPI: Framework para construir APIs rápidas y eficientes en Python.
-SQLAlchemy: ORM para interactuar con la base de datos PostgreSQL.
-PostgreSQL: Motor de base de datos relacional.
-Docker: Contenerización de la aplicación.

### Instalación y Configuración

-Prerequisitos
Asegúrate de tener Docker y Docker Compose instalados en tu sistema.

-Construir y Levantar la Aplicación
Construir las imágenes de Docker:
docker-compose build

Levantar los contenedores:
docker-compose up

-Variables de Entorno
Asegúrate de configurar las variables de entorno para la base de datos en el archivo docker-compose.yml. Por defecto, se usa PostgreSQL con el usuario y contraseña postgres, y la base de datos leads_db.
environment:
  POSTGRES_USER: postgres
  POSTGRES_PASSWORD: postgres
  POSTGRES_DB: leads_db

### Endpoints (Solo Leads)

-Crear un Lead
Método: POST
URL: /api/leads/
Descripción: Crea un nuevo lead con materias asociadas.
Cuerpo de la Solicitud (JSON):
{
  "name": "Juan Pérez",
  "email": "juan.perez@example.com",
  "address": "Calle Falsa 123, Ciudad",
  "phone": "+1234567890",
  "registration_year": 2023,
  "subjects": [
    {
      "name": "Matemáticas",
      "career": "Ingeniería",
      "duration": 16,
      "registration_year": 2023,
      "times_taken": 1
    },
    {
      "name": "Física",
      "career": "Ingeniería",
      "duration": 14,
      "registration_year": 2023,
      "times_taken": 2
    }
  ]
}
Respuesta (JSON):
{
  "id": 1,
  "name": "Juan Pérez",
  "email": "juan.perez@example.com",
  "address": "Calle Falsa 123, Ciudad",
  "phone": "+1234567890",
  "registration_year": 2023,
  "subjects": [
    {
      "id": 1,
      "name": "Matemáticas",
      "career": "Ingeniería",
      "duration": 16,
      "registration_year": 2023,
      "times_taken": 1,
      "lead_id": 1
    },
    {
      "id": 2,
      "name": "Física",
      "career": "Ingeniería",
      "duration": 14,
      "registration_year": 2023,
      "times_taken": 2,
      "lead_id": 1
    }
  ]
}

Leer Leads
Método: GET
URL: /api/leads/
Descripción: Obtiene una lista de leads. Puedes usar parámetros skip y limit para paginar.
Parámetros de Consulta:

skip: Número de resultados a omitir (paginación).
limit: Número máximo de resultados a devolver.
Respuesta (JSON):
[
  {
    "id": 1,
    "name": "Juan Pérez",
    "email": "juan.perez@example.com",
    "address": "Calle Falsa 123, Ciudad",
    "phone": "+1234567890",
    "registration_year": 2023,
    "subjects": [...]
  },
  ...
]
Leer un Lead por ID
Método: GET
URL: /api/leads/{lead_id}
Descripción: Obtiene un lead específico por su ID.
Respuesta (JSON):

{
  "id": 1,
  "name": "Juan Pérez",
  "email": "juan.perez@example.com",
  "address": "Calle Falsa 123, Ciudad",
  "phone": "+1234567890",
  "registration_year": 2023,
  "subjects": [...]
}

### Testing

Para probar la API, puedes utilizar herramientas como Postman o curl. También puedes ejecutar pruebas unitarias utilizando pytest. Para esto, utiliza el siguiente comando:

docker-compose run --rm test

-Pruebas
Pruebas Unitarias: Verifica que los métodos y clases de la API funcionen como se espera.
Pruebas de Integración: Verifica que los endpoints de la API funcionen correctamente en conjunto.

### Documentación de la API

La API está documentada automáticamente por FastAPI. Puedes acceder a la documentación interactiva en:

Swagger UI: http://localhost:8000/docs
ReDoc: http://localhost:8000/redoc