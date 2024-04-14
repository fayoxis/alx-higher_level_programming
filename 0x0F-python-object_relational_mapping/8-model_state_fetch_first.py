#!/usr/bin/python3
"""Script that prints the first State object from the database
hbtn_0e_6_usa"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Check if the required command-line arguments are provided
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database_name>")
        sys.exit(1)

    # Unpack the command-line arguments
    username, password, database_name = sys.argv[1], sys.argv[2], sys.argv[3]

    # Create the SQLAlchemy engine and session
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost/{database_name}',
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Retrieve all the State objects and print the result
    states = session.query(State).order_by(State.id).all()
    if states:
        for state in states:
            print(f"{state.id}: {state.name}")
    else:
        print("Nothing")

    # Close the session
    session.close()
