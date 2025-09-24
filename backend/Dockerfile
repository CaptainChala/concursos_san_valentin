# Dockerfile para Django Backend
FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install gunicorn

COPY . .

ENV PYTHONUNBUFFERED=1

# Variables de entorno para correo (puedes cambiar en docker-compose)
ENV EMAIL_USER=tu_email@hotmail.com
ENV EMAIL_PASS=tu_password

CMD ["gunicorn", "concurso.wsgi:application", "--bind", "0.0.0.0:8000"]
