#!/usr/bin/python3
"""this Script will creates State with the City
from the database """

if __name__ == '__main__':
    from sys import argv, exit
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from relationship_state import Base, State
    from relationship_city import City

    if len(argv) != 4:
        exit('Use: 100-relationship_states_cities.py <mysql username> '
             '<mysql password> <database name>')

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/'
                           '{}'.format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    session = Session(engine)
    Base.metadata.create_all(engine)  # creates decprecated warning 1681

    new_state = State(name='California')
    new_city = City(name='San Francisco', state_id=new_state.id)
    new_state.cities.append(new_city)
    session.add_all([new_state, new_city])
    session.commit()
    session.close()
