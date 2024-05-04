#!/usr/bin/python3
"""Module Documentaion"""

import sqlalchemy
import sys
from sqlalchemy import MetaData, create_engine
from model_state import State, Base
from sqlalchemy.orm import session, sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                                                     sys.argv[1],
                                                     sys.argv[2],
                                                     sys.argv[3],
                                                     ),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(
        State.id).filter(State.name.like(sys.argv[4])).first()
    if states:
        print("{}".format(states.id))
    else:
        print("Not found")

    session.close()