# Используем официальный образ Python в качестве базового
FROM python:3.9-slim

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем файл requirements.txt в рабочую директорию
COPY requirements.txt .

# Устанавливаем зависимости из requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Копируем ваш скрипт в рабочую директорию
COPY QuoteBot.py .

# Указываем команду, которая будет выполнена при запуске контейнера
CMD ["python", "QuoteBot.py"]
