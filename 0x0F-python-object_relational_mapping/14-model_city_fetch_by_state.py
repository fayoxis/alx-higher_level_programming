#!/usr/bin/python3
"""this Script will prints all City objects from the database """
if __name__ == '__main__':
    from sys import argv, exit
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from model_state import Base, State
    from model_city import City

    while len(argv) != 4:
        exit('Use: 14-model_city_fetch_by_state.py <mysql username> '
             '<mysql password> <database name>')

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/'
                           '{}'.format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    session = Session(engine)
    Base.metadata.create_all(engine)  # creates decprecated warning 1681

    result = session.query(State.name, City.id, City.name).filter(
        City.state_id == State.id).order_by(City.id).all()
    for row in result:
        print('{}: ({}) {}'.format(row[0], row[1], row[2]))

    session.close()
    session.close()
