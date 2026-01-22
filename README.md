# Django Chat API

Django Chat API — это REST API для управления чатами и сообщениями, разработанное на Django REST Framework. Проект предоставляет полный набор операций CRUD для работы с чат-комнатами и сообщениями, включая валидацию данных, каскадное удаление и пагинацию.

## Ключевые особенности

- **Полное API** — 4 эндпоинта для работы с чатами и сообщениями
- **Валидация данных** — автоматическая проверка входных параметров
- **Docker-контейнеризация** — PostgreSQL и Django в отдельных контейнерах
- **Каскадное удаление** — автоматическое удаление сообщений при удалении чата
- **Пагинация** — ограничение количества возвращаемых сообщений
- **Тестирование** — юнит-тесты для всех API эндпоинтов

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
### Доступ к приложению
#### После запуска приложение доступно по адресам:

API Endpoints: http://localhost:8000/api/chats/

Админ-панель: http://localhost:8000/admin/


### API Документация
#### Модели:
- Chat: id, title (1-200 символов), created_at
- Message: id, chat_id (FK), text (1-5000 символов), created_at

#### Эндпоинты:
#### 1. Создание чата
POST /api/chats/
```
{
  "title": "Название чата"
}
```

#### 2. Получение чата с сообщениями
GET /api/chats/{id}/?limit=20
- limit: количество сообщений (по умолчанию 20, максимум 100)
- Сообщения сортируются по created_at

#### 3. Отправка сообщения
POST /api/chats/{id}/messages/
```
{
  "text": "Текст сообщения"
}
```

#### 4. Удаление чата
DELETE /api/chats/{id}/

- Удаляет чат и все связанные сообщения (каскадное удаление)

### Валидация
title: не пустой, 1-200 символов, обрезка пробелов

text: не пустой, 1-5000 символов

404 ошибка при попытке отправить сообщение в несуществующий чат
