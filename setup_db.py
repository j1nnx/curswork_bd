import psycopg2


def create_database():
    """This function is responsible for creating a database table"""
    # connect with my database
    conn = psycopg2.connect(dbname='postgres', user='postgres', password='simplepassword123', host='localhost')
    conn.autocommit = True
    cursor = conn.cursor()
    # Install database in my project
    cursor.execute("DROP DATABASE IF EXISTS hh_vacancies;")
    cursor.execute("CREATE DATABASE hh_vacancies;")
    cursor.close()
    conn.close()


#
def create_tables():
    """create db table"""
    conn = psycopg2.connect(dbname='hh_vacancies', user='postgres', password='simplepassword123', host='localhost')
    cursor = conn.cursor()

    # first table companies
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS companies (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            description TEXT,
            vacancies_url VARCHAR(255)
        );
    """)

    # second table vacanciess
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS vacancies (
            id SERIAL PRIMARY KEY,
            title VARCHAR(255) NOT NULL,
            salary INTEGER,
            url VARCHAR(255),
            company_id INTEGER REFERENCES companies(id) ON DELETE CASCADE
        );
    """)

    conn.commit()
    cursor.close()
    conn.close()


def add_company(conn, name, description, vacancies_url):
    """
    Adds a company to the companies table.
    """
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO companies (name, description, vacancies_url) 
        VALUES (%s, %s, %s) RETURNING id;
    """, (name, description, vacancies_url))
    company_id = cursor.fetchone()[0]
    conn.commit()
    cursor.close()
    return company_id


def add_vacancy(conn, title, salary, url, company_id):
    """
    Adds a vacancy to the vacancies table.
    """
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO vacancies (title, salary, url, company_id) 
        VALUES (%s, %s, %s, %s);
    """, (title, salary, url, company_id))
    conn.commit()
    cursor.close()
