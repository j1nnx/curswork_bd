import psycopg2
from configparser import ConfigParser


def config(filename='database.ini', section='postgresql'):
    """Читает параметры подключения из файла конфигурации."""
    parser = ConfigParser()
    parser.read(filename)

    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception(f"Секция {section} не найдена в файле {filename}")

    return db


def get_all_data_from_tables():
    """Подключается к базе данных, получает список таблиц и выводит все данные из каждой таблицы."""
    params = config()

    conn = psycopg2.connect(**params)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT table_name
        FROM information_schema.tables
        WHERE table_schema = 'public'
    """)

    tables = cursor.fetchall()

    for table in tables:
        table_name = table[0]
        print(f"\nТаблица: {table_name}")

        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()

        column_names = [desc[0] for desc in cursor.description]
        print(" | ".join(column_names))

        for row in rows:
            print(" | ".join(str(value) if value is not None else 'NULL' for value in row))

    cursor.close()
    conn.close()

get_all_data_from_tables()
