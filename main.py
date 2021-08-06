import random as rand

import mysql.connector
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.sql import text


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
    db_cursor.execute('CREATE DATABASE game_db')
    db_cursor.execute('SHOW DATABASES')

    for row in db_cursor:
        print(row)

    db_cursor.close()
    db_connection.close()


def create_table(metadata, engine):
    players = Table(
        'players', metadata,
        Column('id', Integer(), primary_key=True),
        Column('nickname', String(32), nullable=False, unique=True),
        Column('level', Integer(), nullable=False, unique=False),
        Column('mojo', Integer(), nullable=False, unique=False),
        Column('intellect', Integer(), nullable=False, unique=False),
        Column('strength', Integer(), nullable=False, unique=False),
        Column('agility', Integer(), nullable=False, unique=False),
        Column('stamina', Integer(), nullable=False, unique=False)
    )
    metadata.create_all(engine)
    return players


def insert_data(players, connection):
    queries = []
    for i in range(25):
        vals = []
        for k in range(7):
            vals.append(rand.randint(0, 100))
        insert_query = players.insert().values(
            nickname=f'name_{i}{chr(vals[0])}{str(vals[0])}',
            level=vals[1],
            mojo=vals[2],
            intellect=vals[3],
            strength=vals[4],
            agility=vals[5],
            stamina=vals[6]
        )
        queries.append(insert_query)

    for query in queries:
        result = connection.execute(query)


def select_smth(players, connection):
    slc = players.select().order_by(text('level desc'))
    result = connection.execute(slc)
    print('\n\n')
    for row in result:
        print(row)


def main():
    # Receiving parameters for the connection.
    args = [*input_connection_values()]

    create_db(lgn=args[0], pwd=args[1], addr=args[2])

    # Creating new connection and metadata object.
    engine = create_engine(f'mysql+mysqlconnector://{args[0]}:{args[1]}@{args[2]}/game_db', echo=True)
    connection = engine.connect()
    metadata = MetaData()

    players = create_table(metadata, engine)
    insert_data(players, connection)
    select_smth(players, connection)


if __name__ == '__main__':
    main()
