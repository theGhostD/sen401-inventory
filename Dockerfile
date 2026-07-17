FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY models.py controllers.py utils.py migrate.py app.py ./

# Data lives on a shared volume so the sqlite-web service can browse it
ENV INVENTORY_DB=/data/inventory.db

# Migrate (idempotent), run the demo, then keep the container alive so
# `docker compose ps` shows a running service and the DB stays browsable
CMD ["sh", "-c", "python migrate.py && python app.py && tail -f /dev/null"]
