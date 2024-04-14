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

    mysql_username = argv[1]
    mysql_password = argv[2]
    database_name = argv[3]

    engine = create_engine(
        f'mysql+mysqldb://{mysql_username}:{mysql_password}@localhost:3306/{database_name}',
        pool_pre_ping=True
    )

    session = Session(engine)
    Base.metadata.create_all(engine)  # creates deprecated warning 1681

    states_and_cities = [
        {'state_name': 'California', 'city_name': 'San Francisco'},
        # Add more state-city pairs here
    ]

    for state_and_city in states_and_cities:
        new_state = State(name=state_and_city['state_name'])
        new_city = City(name=state_and_city['city_name'], state_id=new_state.id)
        new_state.cities.append(new_city)
        session.add_all([new_state, new_city])

    session.commit()
    session.close()
