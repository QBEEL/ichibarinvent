# Установим необходимые пакеты для компиляции
RUN apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    libffi-dev \
    python3-dev \
    libpq-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Создаем виртуальное окружение и устанавливаем зависимости
RUN python -m venv /opt/venv
RUN . /opt/venv/bin/activate && pip install --upgrade pip
RUN . /opt/venv/bin/activate && pip install -r requirements.txt
