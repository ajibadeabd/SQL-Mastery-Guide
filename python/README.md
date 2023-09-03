# SQL-Mastery-Guide

Welcome to the SQL Mastery Guide! This repository is designed to be your comprehensive resource for mastering SQL (Structured Query Language). Whether you're a beginner or an experienced developer looking to deepen your SQL skills, this guide has something for everyone.

## SQL create table

In this section, we provide a Python script that simplifies the process of creating database tables from SQL statements. The Python script reads an SQL file containing table creation queries and executes them in your chosen database system. This automation helps streamline the setup of database tables, allowing you to focus on learning SQL.

### Python Script Description

The Python script, `create_tables.py`, serves the following purposes:

- Reads an SQL file containing table creation queries.
- Splits the SQL file into individual queries.
- Connects to your database.
- Executes each query to create the specified tables.


**Note**: It's important to create the tables in the correct order to avoid errors. For example, creating the "Books" table before the "Authors" table may result in an error if the "Authors" table does not exist yet. Ensure the order of table creation matches the dependencies between tables in your database schema.


### Usage

1. Specify the path to your SQL file containing table creation queries in the `sql_file` variable within the script.
2. Configure the database connection settings within the script.
3. Run the `create_tables.py` script using Python.

Ensure you have the necessary database system installed and a database created before running the script. The script is designed to work with various database systems, but you may need to install the corresponding database library (e.g., `sqlite3` for SQLite) and modify the connection details accordingly.

Feel free to explore the SQL Mastery Guide to learn more about SQL fundamentals, database management systems, and practical projects to enhance your SQL skills.

Happy learning!
