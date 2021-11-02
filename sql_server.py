'''
Basic SQL server operators using mysql-connector and sqlalchemy
'''

from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError

HOST = '192.168.1.2'
USER = 'root'
PASS = 'G3nerationIO'
DB = 'eve'


def create_sqlalch_engine(host_name=HOST, user_name=USER, user_password=PASS, db_name=DB):
    try:
        engine = create_engine(f"mysql+pymysql://{user_name}:{user_password}@{host_name}/{db_name}")
        print("Engine creation successful")
    except SQLAlchemyError as err:
        print(f"Error: '{err}'")
    return engine


def execute_alch_query(engine, query):
    try:
        res = engine.execute(query)
        print("Query successful")
    except SQLAlchemyError as err:
        print(f"Error: '{err}'")
    return res


if __name__ == "__main__":
    create_sqlalch_engine()
