# Usa una imagen base oficial de Python
FROM python:3.11-slim

# Establece el directorio de trabajo
WORKDIR /app

# Variables de entorno
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Instala dependencias del sistema necesarias para compilar mysqlclient
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    gcc \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Copia e instala dependencias de Python
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copia el código del proyecto
COPY . /app/

# Expone el puerto
EXPOSE 8000

# Comando para producción (usando gunicorn)
CMD ["gunicorn", "mi_examen_crud.wsgi:application", "--bind", "0.0.0.0:8000"]
