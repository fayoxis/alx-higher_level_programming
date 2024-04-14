#!/usr/bin/python3
"""Script prints the object with the name passed as argument from
the database """


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    if len(sys.argv) < 5:
        print("Usage: python script.py <username> <password> <database_name> <state_name>")
        sys.exit(1)
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    # Create the database engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        username, password, database_name), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the State table for the given state name
    state = session.query(State).filter_by(name=state_name).first()
    if state:
        print("{}".format(state.id))
    else:
        print("Not found")

    # Close the session
    session.close()
