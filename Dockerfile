# 1. Usamos una imagen ligera de Python estable
FROM python:3.11-slim

# 2. Evitamos que Python genere archivos basura (.pyc)
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 3. Directorio de trabajo dentro del contenedor
WORKDIR /app

# 4. Instalamos dependencias del sistema necesarias para torch
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# 5. Copiamos el archivo de requisitos e instalamos librerías
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 6. Copiamos el código
COPY . .

EXPOSE 8501
# 7. Comando para ejecutar tu IA
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]