# Usa una imagen base oficial de Python
FROM python:3.11-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Instala dependencias necesarias para mysqlclient
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    gcc \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

# Expone el puerto de Django
EXPOSE 8000

# ⚠️ ESTE COMANDO DEBE ESTAR PRESENTE AL FINAL
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
