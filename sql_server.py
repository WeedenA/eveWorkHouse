'''
Basic SQL server operators using mysql-connector and sqlalchemy
todo: scrub personal before upload
'''

import mysql.connector
from mysql.connector import Error
# from PriceData import PriceData
from sqlalchemy import create_engine
from sqlalchemy.types import Date, Integer
from sqlalchemy.exc import SQLAlchemyError
import pandas as pd


HOST = '192.168.1.2'
USER = 'root'
PASS = 'G3nerationIO'
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


def create_database(connection, db_name):
    cursor = connection.cursor()
    try:
        cursor.execute(f"CREATE DATABASE {db_name}")
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


def create_sqlalch_engine(host_name=HOST, user_name=USER, user_password=PASS, db_name=DB):
    try:
        engine = create_engine(f"mysql+pymysql://{user_name}:{user_password}@{host_name}/{db_name}")
        print("Engine creation successful")
    except SQLAlchemyError as err:
        print(f"Error: '{err}'")
    return engine


def execute_alch_query(engine, query):
    try:
        res = engine.execute(query).fetchall()
        print("Query successful")
    except SQLAlchemyError as err:
        print(f"Error: '{err}'")
    return res


# def migrate_pickle_to_sqldb():
#     engine = create_sqlalch_engine(HOST, USER, PASS, DB)
#     handler = PriceData()
#     log = handler.openLog()
#
#     df = pd.DataFrame(log)
#     df.to_sql('ore_price_record', engine, index=False, index_label="date", if_exists='replace',
#               dtype={"date": Date(), 'Loparite': Integer(), 'Monazite': Integer(),
#                      'Xenotime': Integer(), 'Ytterbite': Integer(),
#                      'Carnotite': Integer(), 'Cinnabar': Integer(), 'Pollucite': Integer(), 'Zircon': Integer(),
#                      'Chromite': Integer(), 'Otavite': Integer(), 'Sperrylite': Integer(), 'Vanadinite': Integer()})
#     print(pd.read_sql_query("SELECT * FROM ore_price_record", engine))
#     print(engine.execute("SELECT * FROM ore_price_record").fetchall())




create_price_table = """
CREATE TABLE ore_price_log (
    ore VARCHAR(20) PRIMARY KEY,
    date DATE,
    price INT 
    );
"""

if __name__ == "__main__":
    pass
