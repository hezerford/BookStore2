# Устанавливаем базовый образ
FROM python:3.12-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Устанавливаем системные зависимости для PostgreSQL
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем Poetry
RUN pip install --no-cache-dir poetry

# Копируем pyproject.toml и poetry.lock для установки зависимостей
COPY pyproject.toml poetry.lock /app/

# Устанавливаем зависимости
RUN poetry config virtualenvs.create false && poetry install --no-root --no-dev

# Копируем всё содержимое проекта в контейнер
COPY . /app

# Устанавливаем рабочую директорию для запуска manage.py
WORKDIR /app/src

# Указываем порт, на котором будет работать приложение
EXPOSE 8000

# Команда запуска приложения
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]