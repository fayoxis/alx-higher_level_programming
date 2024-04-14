#!/usr/bin/python3
"""this Script lists all State objects that in the database
"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Connect to the MySQL database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    
    # Create the database tables
    Base.metadata.create_all(engine)
    
    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()
    
    for state in session.query(State).filter(State.name.like(
         '%a%')).order_by(State.id):
        print("{}: {}".format(state.id, state.name))
    
    # Close the session
    session.close()
