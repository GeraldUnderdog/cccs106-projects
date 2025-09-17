import mysql.connector
from mysql.connector import Error

def connect_db():
    """
    Establishes and returns a connection to the MySQL database.
    
    Returns:
        mysql.connector.connection.MySQLConnection: A connection object if successful, None otherwise.
    """
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Ridge1228",  # Using the same password as in main.py
            database="fletapp"
        )
        return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        raise e
