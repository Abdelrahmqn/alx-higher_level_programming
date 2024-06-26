#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_state import State
from model_city import Base, City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1],
                                                    sys.argv[2], sys.argv[3]),
        pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(City.name,
                          State.name,
                          City.id).filter(State.id == City.state_id)
    for argn in query:
        print("{}: ({}) {}".format(argn[1], argn[2], argn[0]))

    session.close()
