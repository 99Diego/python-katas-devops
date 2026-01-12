FROM python:3.12-slim

# Seguridad y buenas prácticas
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Dependencias del sistema (mínimas)
RUN apt-get update \
    && apt-get install -y --no-install-recommends curl \
    && rm -rf /var/lib/apt/lists/*

# Copiar requirements y instalar
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Código de la aplicación
COPY app ./app

# Usuario no root
RUN useradd -m appuser
USER appuser

# Puerto expuesto
EXPOSE 8000

# Healthcheck
HEALTHCHECK CMD curl --fail http://localhost:8000/health || exit 1

# Comando de arranque
CMD ["uvicorn", "app.api.main:app", "--host", "0.0.0.0", "--port", "8000"]
