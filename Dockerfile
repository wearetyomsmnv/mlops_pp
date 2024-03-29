   # Выбор базового образа
   FROM python:3.8-slim
   
   # Установка рабочей директории в контейнере
   WORKDIR /app
   
   # Копирование файлов зависимостей
   COPY requirements.txt .
   
   # Установка зависимостей
   RUN pip install --no-cache-dir -r requirements.txt
   
   # Копирование исходного кода проекта в контейнер
   COPY . .
   
   # Указание команды для запуска при старте контейнера
   CMD ["python", "train.py"]
   
