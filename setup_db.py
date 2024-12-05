import psycopg2


def create_database():
    """Creates the main database for storing company and vacancy data."""
    # Connect in my database
    conn = psycopg2.connect(dbname='postgres', user='postgres', password='simplepassword123', host='localhost')
    conn.autocommit = True
    # Open cursor from my database
    cursor = conn.cursor()

    # Drops the database if it exists to avoid conflicts.
    cursor.execute("DROP DATABASE IF EXISTS hh_vacancies;")
    # Creates a new database named `hh_vacancies`.
    cursor.execute("CREATE DATABASE hh_vacancies;")
    cursor.close()  # Close cursor in my database
    conn.close()  # Close connect in my database


def create_tables():
    """Defines and creates the database tables for storing company and vacancy data."""
    # Connect in my database
    conn = psycopg2.connect(dbname='hh_vacancies', user='postgres', password='simplepassword123', host='localhost')
    # Open cursor from my database
    cursor = conn.cursor()

    # Table for storing companies and their details.
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS companies (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            description TEXT,
            vacancies_url VARCHAR(255)
        );
    """)

    # Table for storing vacancies and linking them to companies.
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS vacancies (
            id SERIAL PRIMARY KEY,
            title VARCHAR(255) NOT NULL,
            salary INTEGER,
            url VARCHAR(255),
            company_id INTEGER REFERENCES companies(id) ON DELETE CASCADE
        );
    """)

    conn.commit()  # Saves all changes.
    cursor.close()  # Close cursor in my database
    conn.close()  # Close connect in my database


def add_company(conn, name, description, vacancies_url):
    """
    Inserts a new company record into the `companies` table.
    Returns the ID of the newly inserted company.
    """
    # Open cursor from my database
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO companies (name, description, vacancies_url) 
        VALUES (%s, %s, %s) RETURNING id;
    """, (name, description, vacancies_url))
    company_id = cursor.fetchone()[0]  # Fetches the generated ID.
    conn.commit()  # Close connect in my database
    cursor.close()  # Close cursor in my database
    return company_id


def add_vacancy(conn, title, salary, url, company_id):
    """
    Inserts a new vacancy record into the `vacancies` table.
    Links the vacancy to its corresponding company.
    """
    # Open cursor from my database
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO vacancies (title, salary, url, company_id) 
        VALUES (%s, %s, %s, %s);
    """, (title, salary, url, company_id))
    conn.commit()  # Close connect in my database
    cursor.close()  # Close cursor in my database
