Nombre del Proyecto

Breve descripción del proyecto:
> Este proyecto es una aplicación web full-stack que permite [describir funcionalidad principal]. Se implementó como monorepo con Docker, de manera que backend y frontend se ejecutan simultáneamente con un solo comando.

------------------------------------------------------------

Tecnologías utilizadas

Backend:
- Python 3.13
- Django 4.x
- Django Rest Framework
- Celery + Redis (para tareas asíncronas)
- sqlite

Frontend:
- Vue.js 3 
- Axios (para consumir APIs)
- node 20

Otros:
- Docker y Docker Compose para levantar ambos entornos simultáneamente

------------------------------------------------------------

Instalación y ejecución

1. Clonar el repositorio: git clone https://github.com/CaptainChala/concursos_san_valentin

2. Construir y ejecutar los contenedores Docker

3. crear archivo .env en backend/.env

4. Luego con el siguiente formato ingresar datos que de los cuales se necesita ocupar el correo como host: 
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=xxxxxx@gmail.com # necesitas agregar un correo, host para poder enviar correos automatizados.
EMAIL_HOST_PASSWORD=xxxx xxxx xxxx xxxx # gmail app password

*Informarse en el siguiente link sobre como conseguir una gmail app password:
 https://support.google.com/mail/answer/185833?hl=es-419
 https://support.google.com/mail/thread/205453566/how-to-generate-an-app-password?hl=en

5. Ejecutar docker-compose up --build en carpeta raiz del proyecto, lo que generará un contenedor, que dentro del mismo orquestará otros 4 contenedores. 

6. El backend estará disponible en:
http://localhost:8000

7. El frontend estará disponible en:
http://localhost:3000

> Con Docker, no es necesario instalar dependencias ni configurar bases de datos localmente; todo está incluido en los contenedores.

------------------------------------------------------------

Decisiones técnicas

- Monorepo con Docker: Permite levantar backend y frontend con un solo comando, asegurando consistencia en versiones y dependencias.
- Django Rest Framework: Facilita la creación de APIs REST robustas y extensibles.
- Celery + Redis: Manejo de tareas asíncronas (ej. envío de correos o procesamiento de datos).
- Frontend separado: Mantener frontend desacoplado del backend permite escalar o reemplazar la interfaz sin afectar la lógica del servidor.

------------------------------------------------------------

Endpoints principales

Registro de usuario
- POST /api/register/
Request:
{
  "username": "usuario",
  "email": "correo@dominio.com",
  "password": "contraseña123"
}
Response:
{
  "id": 1,
  "username": "usuario",
  "email": "correo@dominio.com"
}

Login
- POST /api/login/
Request:
{
  "username": "usuario",
  "password": "contraseña123"
}
Response:
{
  "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
}

Obtener lista de ítems
- GET /api/items/
Response:
[
  {
    "id": 1,
    "name": "Item 1",
    "description": "Descripción del item"
  },
  {
    "id": 2,
    "name": "Item 2",
    "description": "Descripción del item"
  }
]

------------------------------------------------------------

Screenshots / GIFs

Pantalla principal: screenshots/home.png
API en funcionamiento: screenshots/api.png

------------------------------------------------------------

Comandos útiles

- Levantar contenedores en background:
docker-compose up -d

- Detener contenedores:
docker-compose down

- Ver logs:
docker-compose logs -f

------------------------------------------------------------

> Con esta configuración, cualquier desarrollador puede clonar el proyecto y ponerlo en funcionamiento sin necesidad de instalar dependencias locales adicionales.
