import json
import getpass
import psycopg


def main():
    with open("app/config.json", "r", encoding="utf-8") as f:
        config = json.load(f)

    login = input("Введите логин: ")
    password = getpass.getpass("Введите пароль: ")

    try:
        conn = psycopg.connect(
            host=config["host"],
            port=config["port"],
            dbname=config["database"],
            user=login,
            password=password
        )

        cursor = conn.cursor()

        cursor.execute("SELECT VERSION()")
        result = cursor.fetchone()

        print("\nПодключение к базе данных выполнено.")
        print("Версия PostgreSQL:", result[0])

        cursor.close()
        conn.close()

    except Exception as e:
        print("Ошибка подключения:", e)


if __name__ == "__main__":
    main()