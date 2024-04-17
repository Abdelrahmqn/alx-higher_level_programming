#!/usr/bin/python3
# when you define a subclass of dec_base() sqlalchemy adds id column even if
# you didn't declare it
# the magic of SQLAlchemy!!
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
                                                     sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    state_name = session.query(State).filter(State.id.like(2)).first()
    state_name.name = 'New Mexico'
    session.commit()

    session.close()
