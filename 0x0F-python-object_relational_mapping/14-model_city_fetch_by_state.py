#!/usr/bin/python3
"""this Script will prints all City objects from the database """
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python script.py <username> <password> <database_name>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        username, password, database_name)
    engine = create_engine(db_uri)
    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(City, State).join(State)

    for _c, _s in query.all():
        print("{}: ({:d}) {}".format(_s.name, _c.id, _c.name))
    session.commit()
    session.close()
