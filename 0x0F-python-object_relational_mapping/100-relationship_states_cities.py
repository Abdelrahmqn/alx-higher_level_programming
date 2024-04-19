#!/usr/bin/python3
"""creates a new state with a new city"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    active = Session()

    state_name = State(name='California')
    city_name = City(name='San Francisco')
    state_name.cities.append(city_name)
    active.add(state_name)
    active.add(city_name)
    active.commit()
