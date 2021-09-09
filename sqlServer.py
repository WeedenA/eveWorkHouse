'''
Basic SQL server operators
todo: scrub personal before upload
'''


import mysql.connector
from mysql.connector import Error
import pandas as pd

HOST = '****'
USER = 'root'
PASS = '****'
DB = 'eve'


def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            passwd = user_password,
        )
        print("Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection


def create_database_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            passwd = user_password,
            database = db_name
        )
        print("Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection


def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database creation successful")
    except Error as err:
        print(f"Error: '{err}'")


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")

create_price_table = """
CREATE TABLE ore_price_log (
    ore VARCHAR(20) PRIMARY KEY,
    date DATE,
    price INT 
    );
"""

if __name__ == "__main__":

    connection = create_database_connection(HOST, USER, PASS, DB)
    execute_query(connection, create_price_table)
