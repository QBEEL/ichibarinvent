# Используем официальный образ Python
FROM python:3.9-slim

# Установим необходимые пакеты для компиляции
RUN apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    libffi-dev \
    python3-dev \
    libpq-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем все файлы из проекта в контейнер
COPY . /app

# Создаем виртуальное окружение
RUN python -m venv /opt/venv

# Активируем виртуальное окружение и обновляем pip
RUN . /opt/venv/bin/activate && pip install --upgrade pip setuptools wheel

# Устанавливаем зависимости из requirements.txt
RUN . /opt/venv/bin/activate && pip install -r requirements.txt

# Экспонируем порт, если нужно
EXPOSE 5000

# Запускаем приложение
CMD ["/opt/venv/bin/python", "main.py"]
