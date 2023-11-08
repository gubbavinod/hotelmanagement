import mysql.connector


# Database connection parameters
db_params = {
    "host": "database-1.cy9obdjndpoc.ap-south-1.rds.amazonaws.com",  # Replace with your RDS endpoint
    "database": "database1",  # Replace with your database name
    "user": "Master",  # Replace with your username
    "password": "Master1234",  # Replace with your password
    "port": "3306",  # Replace with your database port (MySQL default is 3306)
}

def create_connection():
    """Establishes a connection to the MySQL database."""
    try:
        connection = mysql.connector.connect(**db_params)
        return connection
    except mysql.connector.Error as e:
        print(f"Error creating connection: {e}")
        return None

def close_connection(connection):
    """Closes the database connection."""
    if connection.is_connected():
        connection.close()
        print("Connection closed.")

def get_items_by_cuisine(cuisine):
    """Retrieves the list of items from the 'meal_info_updated' table based on the specified cuisine."""
    try:
        connection = create_connection()
        if connection:
            cursor = connection.cursor()
            query = "SELECT Item FROM meal_information WHERE Cuisine = %s;"
            # Include only necessary fields and filter by cuisine

            cursor.execute(query, (cuisine,))
            rows = cursor.fetchall()

            items_list = [row[0] for row in rows]
            # Just for debugging, print the list of items
            
            data = {'items': items_list}
            cursor.close()
            close_connection(connection)
            return data

    except mysql.connector.Error as e:
        print(f"Error fetching items list by cuisine: {e}")
        return None


def get_items_list():
    """Retrieves the list of items from the 'meal_info_updated' table."""
    try:
        connection = create_connection()
        if connection:
            cursor = connection.cursor()
            query = "SELECT Meal_id, Item, Price FROM meal_information;"  # Include only necessary fields

            cursor.execute(query)
            rows = cursor.fetchall()

            data = []
            for row in rows:
                data.append({
                    "meal_id": row[0],
                    "item": row[1],
                    "price": row[2]
                })
            cursor.close()
            return data

    except mysql.connector.Error as e:
        print(f"Error fetching items list: {e}")
        return None

    finally:
        close_connection(connection)


