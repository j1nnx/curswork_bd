import psycopg2


class DBManager:
    # Initializes the DBManager object and establishes a connection to the database
    def __init__(self, dbname, user, password, host='localhost'):
        """Establishes a connection to the database and creates a cursor for executing queries."""
        self.conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
        self.cursor = self.conn.cursor()

    def get_companies_and_vacancies_count(self):
        """Retrieves the count of vacancies for each company."""
        # Query to count the number of vacancies grouped by company
        self.cursor.execute("""
            SELECT companies.name, COUNT(vacancies.id) AS vacancies_count
            FROM companies
            LEFT JOIN vacancies ON companies.id = vacancies.company_id
            GROUP BY companies.name;
        """)
        return self.cursor.fetchall()

    def get_all_vacancies(self):
        """Retrieves all vacancies along with their associated company details."""
        # Query to fetch all vacancies and their related company details
        self.cursor.execute("""
            SELECT companies.name, vacancies.title, vacancies.salary, vacancies.url
            FROM vacancies
            JOIN companies ON vacancies.company_id = companies.id;
        """)
        return self.cursor.fetchall()

    def get_avg_salary(self):
        """Calculates the average salary of all vacancies."""
        # Query to calculate the average salary from the vacancies table
        self.cursor.execute("SELECT AVG(salary) FROM vacancies;")
        return self.cursor.fetchone()[0]

    def get_vacancies_with_higher_salary(self):
        """Retrieves vacancies with salaries above the average."""
        # Get the average salary first
        avg_salary = self.get_avg_salary()
        # Query to fetch vacancies with salaries greater than the average salary
        self.cursor.execute("""
            SELECT title, salary, url
            FROM vacancies
            WHERE salary > %s;
        """, (avg_salary,))
        return self.cursor.fetchall()

    def get_vacancies_with_keyword(self, keyword):
        """Searches for vacancies containing a specific keyword in their title."""
        # Query to fetch vacancies where the title contains the specified keyword
        self.cursor.execute("""
            SELECT title, salary, url
            FROM vacancies
            WHERE title LIKE %s;
        """, (f'%{keyword}%',))
        return self.cursor.fetchall()