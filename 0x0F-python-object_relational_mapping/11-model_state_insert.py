#!/usr/bin/python3
"""the Script  adds the State object to the
database """
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Connect to the database using the provided credentials
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    
    # Create the database tables if they don't already exist
    Base.metadata.create_all(engine)
    
    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # Create a new State object and add it to the session
    new_state = State(name='Louisiana')
    session.add(new_state)
    
    # Retrieve the newly created State object and print its ID
    state = session.query(State).filter_by(name='Louisiana').first()
    print(str(state.id))
    
    # Commit the changes and close the session
    session.commit()
    session.close()
