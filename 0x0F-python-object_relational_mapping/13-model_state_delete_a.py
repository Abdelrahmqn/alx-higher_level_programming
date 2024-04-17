#!/usr/bin/python3
"""Module Documentaion"""

import sqlalchemy
import sys
from sqlalchemy import create_engine
from model_state import State, Base
from sqlalchemy.orm import session, sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                                                     sys.argv[1],
                                                     sys.argv[2],
                                                     sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    record = session.query(State).order_by(
        State.id).filter(State.name.like('%a%')).all()

    for state in record:
        session.delete(state)

    session.commit()
    session.close()
