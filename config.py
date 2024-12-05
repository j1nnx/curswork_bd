import psycopg2
from configparser import ConfigParser


def config(filename='database.ini', section='postgresql'):
    """Reads connection parameters from a configuration file."""
    parser = ConfigParser()
    parser.read(filename)

    db = {}
    if parser.has_section(section):
        params = parser.items(section)  # Retrieves all options under the specified section.
        for param in params:
            db[param[0]] = param[1]  # Maps option names to their values.
    else:
        raise Exception(f"Section {section} not found in the file {filename}")

    return db


def get_all_data_from_tables():
    """
    Connects to the database and retrieves data from all public tables.
    Outputs each table's content to the console.
    """
    params = config()  # Retrieves database connection parameters.

    conn = psycopg2.connect(**params)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT table_name
        FROM information_schema.tables
        WHERE table_schema = 'public'
    """)

    tables = cursor.fetchall()  # Fetches all table names.

    for table in tables:
        table_name = table[0]
        print(f"\nTable: {table_name}")

        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()

        # Displays column headers.
        column_names = [desc[0] for desc in cursor.description]
        print(" | ".join(column_names))

        # Displays table data row by row.
        for row in rows:
            print(" | ".join(str(value) if value is not None else 'NULL' for value in row))

    cursor.close()
    conn.close()


get_all_data_from_tables()
