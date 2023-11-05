import mysql.connector
# Database connection parameters
db_params = {
    "host": "database-1.cy9obdjndpoc.ap-south-1.rds.amazonaws.com",  # Replace with your RDS endpoint
    "database": "database1",  # Replace with your database name
    "user": "Master",  # Replace with your username
    "password": "Master1234",  # Replace with your password
    "port": "3306",  # Replace with your database port (PostgreSQL default is 5432)
}

try:
    # Establish a database connection
    connection = mysql.connector.connect(**db_params)

    # Create a cursor object
    cursor = connection.cursor()

    # Define your SQL query
    query = "SELECT * FROM meal_info;"  # Replace with your table name

    # Execute the query
    cursor.execute(query)

    # Fetch all rows from the result set
    rows = cursor.fetchall()

    # Process and print the retrieved data
    for row in rows:
        print(row)

except mysql.connector.Error as e:
    print(f"Error: {e}")
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()