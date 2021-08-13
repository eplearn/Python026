import random as rand

import mysql.connector
from sqlalchemy import create_engine, Column, Integer, String, text
from sqlalchemy.ext.declarative import declarative_base


# Base refers to object contains hidden Metadata object and mapper (class -> table).
Base = declarative_base()


class Product(Base):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True)
    name = Column(String(45), nullable=False)
    location = Column(String(45), nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(Integer, nullable=False)
    mass = Column(Integer, nullable=False)


def input_connection_values():
    # Input login and password.
    addr = ''
    lgn = input('Enter your login: ')
    pwd = input('Enter your password: ')
    answer = ''
    while answer != 'y' and answer != 'Y' and answer != 'n' and answer != 'N':
        answer = input('Are you going connect to localhost? Y/N: ')
    if answer == 'y' or answer != 'Y':
        addr = 'localhost'
    elif answer == 'n' or answer != 'N':
        addr = input('Enter database address: ')

    return [lgn, pwd, addr]


def create_db(lgn, pwd, addr):
    db_connection = mysql.connector.connect(
        host=addr,
        user=lgn,
        password=pwd
    )

    db_cursor = db_connection.cursor()
    db_cursor.execute('CREATE DATABASE store_data')
    db_cursor.execute('SHOW DATABASES')

    for row in db_cursor:
        print(row)

    db_cursor.close()
    db_connection.close()


def main():
    # Receiving parameters for the connection.
    args = [*input_connection_values()]

    create_db(lgn=args[0], pwd=args[1], addr=args[2])

    # Creating new connection and metadata object.
    engine = create_engine(f'mysql+mysqlconnector://{args[0]}:{args[1]}@{args[2]}/game_db', echo=True)
    connection = engine.connect()

    Base.metadata.create_all(engine)


if __name__ == "__main__":
    main()
