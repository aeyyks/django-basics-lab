# django-basics-lab

Django-приложение каталога товаров с категориями и продуктами. Использует PostgreSQL, Bootstrap 5 для фронтенда, фикстуры для начальных данных и кастомные manage-команды.

## Стек

- **Python** 3.x / **Django** 6.1.3
- **PostgreSQL** (настройка через `.env`)
- **Bootstrap 5** (статика в `static/`)

## Структура

```
catalog/     — приложение: модели (Category, Product), views, templates, fixtures
config/      — настройки проекта, URL-конфигурация
static/      — CSS/JS Bootstrap 5
```

## Маршруты

| Путь             | Название       | View        |
|------------------|----------------|-------------|
| `/catalog/home/` | home           | `home`      |
| `/catalog/contacts/` | contacts  | `contacts`  |
| `/admin/`        | админ-панель   | Django Admin|

## Установка и запуск

1. Создать `.env` на основе `.env.example`, указать `DB_NAME`, `DB_USER`, `DB_PASSWORD`.
2. Установить зависимости: `pip install -r requirements.txt`.
3. Применить миграции: `python manage.py migrate`.
4. Загрузить начальные данные: `python manage.py fill_db`.
5. Запустить dev-сервер: `python manage.py runserver`.

## Примеры запросов

```bash
# Главная страница
curl http://127.0.0.1:8000/catalog/home/

# Контакты
curl http://127.0.0.1:8000/catalog/contacts/

# Админ-панель
curl -I http://127.0.0.1:8000/admin/
```
