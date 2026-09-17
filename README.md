# Практическое задание №1

Работа с PostgreSQL 18 в Docker

В проекте используются:

* PostgreSQL 18
* Docker
* Adminer
* Python и psycopg

Запустить Docker-контейнеры:

```text
docker compose up -d --build
```

Adminer открывается по адресу `http://localhost:8080`

Для запуска программы:

```text
python app/main.py
```

Программа запрашивает логин и пароль, подключается к базе данных и выводит версию PostgreSQL, при этом пароль не хранится в файле конфигурации

Настройки подключения находятся в `app/config.json`
