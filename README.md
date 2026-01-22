# Django Chat API

Django Chat API — это REST API для управления чатами и сообщениями, разработанное на Django REST Framework. Проект предоставляет полный набор операций CRUD для работы с чат-комнатами и сообщениями, включая валидацию данных, каскадное удаление и пагинацию.

## Ключевые особенности

- **Полное API** — 4 эндпоинта для работы с чатами и сообщениями
- **Валидация данных** — автоматическая проверка входных параметров
- **Docker-контейнеризация** — PostgreSQL и Django в отдельных контейнерах
- **Каскадное удаление** — автоматическое удаление сообщений при удалении чата
- **Пагинация** — ограничение количества возвращаемых сообщений
- **Тестирование** — юнит-тесты для всех API эндпоинтов

## Быстрый старт

### Запуск с Docker (рекомендуется)

```bash
# 1. Клонируйте репозиторий
git clone https://github.com/EvdokimovAnR/chat_api_test.git
cd chat-api_test

# 2. Создайте файл окружения
cp .env

# 3. Запустите через Docker Compose
docker-compose up --build
```
### Запуск без Docker
```
# 1. Клонируйте репозиторий
git clone https://github.com/EvdokimovAnR/chat_api_test.git
cd chat_api_test

# 2. Установите виртуальное окружение
python -m venv venv
source venv/bin/activate  # Linux/Mac
# или
venv\Scripts\activate     # Windows

# 3. Установите зависимости
pip install -r requirements.txt

# 4. Установите и настройте PostgreSQL
# Создайте базу данных и пользователя:
# CREATE DATABASE chat_db;
# CREATE USER chat_user WITH PASSWORD 'password';
# GRANT ALL PRIVILEGES ON DATABASE chat_db TO chat_user;

# 5. Создайте файл окружения
cp .env.example .env

# 6. Примените миграции
python manage.py migrate

# 7. Создайте администратора
python manage.py createsuperuser

# 8. Запустите сервер
python manage.py runserver
```
