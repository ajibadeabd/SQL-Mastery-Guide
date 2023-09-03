import sqlite3

# Specify the path to your SQL file
sql_file = 'create_tables.sql'

def execute_sql_file(database_path, sql_file):
    try:
        # Connect to the database
        conn = sqlite3.connect(database_path)
        cursor = conn.cursor()

        # Read and split the SQL file into individual queries
        with open(sql_file, 'r') as file:
            sql_queries = file.read().split(';')

        # Execute each query
        for query in sql_queries:
            if query.strip():  # Ensure it's not an empty query
                cursor.execute(query)

        # Commit the changes and close the connection
        conn.commit()
        conn.close()
        print("SQL file executed successfully.")

    except Exception as e:
        print("Error:", str(e))

if __name__ == "__main__":
    # Specify the path to your SQLite database file
    db_path = 'your_database.db'

    # Call the function to execute the SQL file
    execute_sql_file(db_path, sql_file)
