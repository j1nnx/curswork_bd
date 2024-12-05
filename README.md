# Project for analyzing vacancies from hh.ru
##### This project collects data on companies and vacancies using the HeadHunter API (hh.ru) and stores it in a PostgreSQL database. The data can be viewed and analyzed via the command line using the user interface implemented in the main module main.py.

## Project structure
### api.py: Module for interacting with the HeadHunter API, containing functions for obtaining data on employers and vacancies.
### db_manager.py: Module for managing the database, includes methods for obtaining statistics and data from the database.
### setup_db.py: Script for creating a database and tables, as well as functions for adding companies and vacancies.
### main.py: The main module that starts the process of creating a database, loading data from the API and providing the user with an interface for working with the data.
### config.py: Displays the contents of tables and vacancies in the table and checks the connection to database.ini
### database.ini: Configuration file with parameters for connecting to the database.