# SDL — Первое практическое задание

## Структура

* `practice1/Dockerfile` — образ PostgreSQL 18
* `practice1/compose.yml` — запуск PostgreSQL и Adminer
* `practice1/postgresql.conf` — настройки PostgreSQL
* `practice1/app/main.py` — приложение для подключения к базе данных
* `practice1/app/config.json` — настройки подключения
* `practice1/requirements.txt` — зависимость Python

Для запуска контейнеров в папке `practice1` и выполнить

```text
docker compose up -d --build
```

Adminer доступен по адресу `http://localhost:8080`.

Для запуска приложения:

```text
python app/main.py
```
