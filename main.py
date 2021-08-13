import random as rand

from psycopg2 import connect, extensions
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

from sqlalchemy import create_engine, Column, Integer, String, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session


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
    # declare a new PostgreSQL connection object
    # A pre-existing database is required in order to create a connection to PostgreSQL (it is 'first' here).
    conn = connect(
        dbname='postgres',
        user=lgn,
        password=pwd,
        host=addr,
        port="5432"
    )

    # object type: psycopg2.extensions.connection
    print("\ntype(conn):", type(conn))

    # string for the new database name to be created
    DB_NAME = "store_data"

    """The psycopg2 adapter will raise an ActiveSqlTransaction exception 
    if you don’t set the connection object’s set_isolation_level attribute.
    This is because the CREATE DATABASE statement won’t work unless AUTOCOMMIT is set to ON."""

    # get the isolation leve for autocommit
    autocommit = extensions.ISOLATION_LEVEL_AUTOCOMMIT
    print("ISOLATION_LEVEL_AUTOCOMMIT:", extensions.ISOLATION_LEVEL_AUTOCOMMIT)

    # set the isolation level for the connection's cursors
    # will raise ActiveSqlTransaction exception otherwise
    conn.set_isolation_level(autocommit)

    # instantiate a cursor object from the connection
    cursor = conn.cursor()

    # use the execute() method to make a SQL request
    cursor.execute('CREATE DATABASE ' + str(DB_NAME))

    # close the cursor to avoid memory leaks
    cursor.close()

    # close the connection to avoid memory leaks
    conn.close()

    print('\n')


def def_location():
    first = rand.randint(1, 4)
    second = rand.randint(1, 4)
    third = rand.randint(1, 4)
    location = {first, second, third}
    return str(location)


def insert_data(session):
    queries = []
    for i in range(25):
        vals = []
        for k in range(4):
            vals.append(rand.randint(0, 100))

        item = Product(
            name=f'name_{i}{chr(vals[0])}',
            location=def_location(),
            quantity=vals[1],
            price=100 * vals[2],
            mass=1000 - vals[3] * rand.randint(0, 5)
        )
        queries.append(item)

    for item in queries:
        session.add(item)
        session.commit()


def select_all(session):
    print('SELECT ALL\n')
    for row in session.query(Product).all():
        print(f'name = {row.name}, location = {row.location}, quantity = {row.quantity}, price = {row.price}, mass = {row.mass}')
    print('\n')


def select_low_mass_items(session):
    print('SELECT LOW MASS AND HIGH PRICE\n')
    for row in session.query(Product).filter(Product.mass < 700, Product.price > 5000).all():
        print(f'name = {row.name}, location = {row.location}, quantity = {row.quantity}, price = {row.price}, mass = {row.mass}')
    print('\n')


def main():
    # Receiving parameters for the connection.
    args = [*input_connection_values()]

    # Creating database 'store_data'.
    create_db(lgn=args[0], pwd=args[1], addr=args[2])

    # Creating new connection.
    engine = create_engine(f'postgresql+psycopg2://{args[0]}:{args[1]}@{args[2]}/store_data', echo=True)
    # connection = engine.connect()

    # Creating table 'product'.
    Base.metadata.create_all(engine)

    # Creating new session.
    session = Session(bind=engine)

    # Adding items to table 'product'.
    insert_data(session)

    # Selecting items in table 'product'.
    select_all(session)
    select_low_mass_items(session)


if __name__ == '__main__':
    main()
