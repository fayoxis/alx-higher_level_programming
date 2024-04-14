#!/usr/bin/python3
"""this Script will creates State with the City
from the database """

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    cities = relationship('City', backref='state')

class City(Base):
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))

if __name__ == "__main__":
    db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        'your_username', 'your_password', 'your_database')
    engine = create_engine(db_uri)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    session = Session()
    cal_state = State(name='California')
    sfr_city = City(name='San Francisco', state=cal_state)
    session.add(cal_state)
    session.add(sfr_city)
    session.commit()
    session.close()
