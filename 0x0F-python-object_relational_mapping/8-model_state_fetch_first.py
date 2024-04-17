#!/usr/bin/python3
"""print the state if id is 1 or
   print the frist"""

import sqlalchemy
import MySQLdb
import sys
from model_state import Base, State

if __name__ == "__main__":
    con = MySQLdb.connect(port=3306, host='localhost', user=sys.argv[1],
                          passwd=sys.argv[2], db=sys.argv[3])
    cur = con.cursor()

    cur.execute("""SELECT id, name FROM states
                   ORDER BY states.id ASC""")

    thisrow = cur.fetchone()
    if thisrow is None:
       exit(1)
    print(*thisrow, sep=': ')

    con.close()


# import sqlalchemy
# import sys
# from sqlalchemy import MetaData, create_engine
# from model_state import State, Base
# from sqlalchemy.orm import session, sessionmaker

# arg1 = sys.argv[1]
# arg2 = sys.argv[2]
# arg3 = sys.argv[3]

# if __name__ == "__main__":
#     engine = create_engine("""mysql+mysqldb://{}:
#                            {}@localhost/{}""".format(arg1,
#                                                      arg2, arg3),
#                            pool_pre_ping=True)
#     Session = sessionmaker(bind=engine)
#     session = Session()

#     states = session.query(State).order_by(State.id).all()
#     for state in states:
#         if state.id == 1:
#             print("{}: {}".format(state.id, state.name))

#     session.close()
