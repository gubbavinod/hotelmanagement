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






''' 
# SQL query to insert values into the 'customers' table
insert_customer_query = """
INSERT INTO customers (username, customer_name, password, phone_number, mail_id)
VALUES (%s, %s, %s, %s, %s);
"""

# Values to insert into the 'customers' table
customer_values = [
    ('santhosh96', 'santhosh nama', 'test123', 8123456789, 'santhoshtest@gmail.com'),
    ('john_doe', 'John Doe', 'password123', 1234567890, 'john.doe@example.com'),
    ('alice_smith', 'Alice Smith', 'alice_password', 9876543210, 'alice.smith@example.com')
]

# Execute the query for each set of values
for values in customer_values:
    execute_query(insert_customer_query, values)

    '''


def execute_query1(query):
    """Connects to the MySQL database, executes the provided query, and returns the result."""
    try:
        connection = mysql.connector.connect(**db_params)
        if connection:
            cursor = connection.cursor()

            # Execute the provided query
            cursor.execute(query)

            # Fetch the result
            result = cursor.fetchall()

            cursor.close()

            return result

    except mysql.connector.Error as e:
        print(f"Error executing query: {e}")
        return None

    finally:
        if connection.is_connected():
            connection.close()
            print("Connection closed.")



def get_pastOrdersDB(orderedby=None):
    """Retrieves the list of items from the 'meal_info_updated' table."""
    try:
        connection = create_connection()
        if connection:
            cursor = connection.cursor()
            if orderedby:
                # Use single quotes around the parameter and parameterize the query
                query = "SELECT id, customername, items, price FROM orders WHERE orderedby = %s;"
                cursor.execute(query, (orderedby,))
            else:
                query = "SELECT id, customername, items, price FROM orders;"
                cursor.execute(query)

            rows = cursor.fetchall()

            data = []
            for row in rows:
                data.append({
                    "id": row[0],
                    "customername": row[1],
                    "items": row[2],
                    "price": row[3]
                })

            cursor.close()
            return data

    except mysql.connector.Error as e:
        print(f"Error fetching items list: {e}")
        return None

    finally:
        close_connection(connection)


query_result=get_pastOrdersDB()

# Example usage:
#query_result = execute_query1("SELECT id,customername,items,price from orders where orderedby='santhosh96'")
#query_result=execute_query1('SELECT id, customername, items, price FROM orders;')



#query_result = execute_query1("""INSERT INTO managers (username, password, name, mailid) VALUES ('manager1', 'test123', 'Kamal Hassan', 'kamal96@gmail.com');""")

if query_result:
    print("Query Result:")
    for row in query_result:
        print(row)
else:
    print("No result or error in executing the query.")

def execute_query(query, values=None):
    """Connects to the MySQL database, executes the provided query with optional values, and returns the result."""
    try:
        connection = mysql.connector.connect(**db_params)
        if connection:
            cursor = connection.cursor()

            # Execute the provided query with optional values
            cursor.execute(query, values)

            # Fetch the result (if applicable)
            result = None
            if cursor.with_rows:
                result = cursor.fetchall()

            # Commit changes to the database
            connection.commit()

            cursor.close()
            return result  # Return the result to the caller

    except mysql.connector.Error as e:
        print(f"Error executing query: {e}")

    finally:
        if connection.is_connected():
            connection.close()
            print("Connection closed.")

def insert_order(customer_name ,items, orderedBy, totalPrice):
    """Inserts a new order into the 'orders' table."""
   
    query = """
    INSERT INTO orders (customername ,items, orderedby, price)
    VALUES (%s, %s, %s, %s);
    """
    values = (customer_name ,items, orderedBy, totalPrice)

    try:
        execute_query(query, values)
        return True
    except:
        return False
    

#insert_order('pawan kalyan' ,'Butter Chicken,Biryani', 'manager', 54)

def insert_customer(customer_name, username, password, mail_id, phone_number):
    """Inserts a new customer into the 'customers' table."""
   
    query = """
    INSERT INTO customers (customer_name, username, password, mail_id, phone_number)
    VALUES (%s, %s, %s, %s, %s);
    """
    values = (customer_name, username, password, mail_id, phone_number)

    try:
        execute_query(query, values)
        return True
    except:
        return False


def insert_manager(name, username, password, mail_id):
    """Inserts a new customer into the 'customers' table."""
   
    query = """
    INSERT INTO managers (name, username, password, mailid)
    VALUES (%s, %s, %s, %s);
    """
    values = (name, username, password, mail_id)

    try:
        execute_query(query, values)
        return True
    except:
        return False
    
#insert_manager(username='manager1', password='test123', name='Kamal Hassan', mail_id='kamal96@gmail.com')    
    
"""



def execute_query12(query, values=None):
    #Connects to the MySQL database, executes the provided query with optional values, and returns the result
    try:
        connection = mysql.connector.connect(**db_params)
        if connection:
            cursor = connection.cursor()

            # Execute the provided query with optional values
            cursor.execute(query, values)

            # Fetch the result (if applicable)
            result = None
            if cursor.with_rows:
                result = cursor.fetchall()

            # Commit changes to the database
            connection.commit()

            cursor.close()
            return result  # Return the result to the caller

    except mysql.connector.Error as e:
        print(f"Error executing query: {e}")

    finally:
        if connection.is_connected():
            connection.close()
            print("Connection closed.")


def customer_authentication(username, password):
 #Authenticates a customer based on username and password
    query = "SELECT * FROM customers WHERE username = %s AND password = %s;"
    values = (username, password)

    result = execute_query12(query, values)

    if result:
        return True
    else:
       
        return False

# Example usage:
username_input = "santhosh96"
password_input = "test123"

customer_authentication(username_input, password_input)

"""

#print(insert_customer(customer_name='mohan Muappalla',username='mohan98',password= 'test123',mail_id= 'mohan98@gmail.com',phone_number= '8323124451'))