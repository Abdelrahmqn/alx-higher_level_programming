#!/usr/bin/python3
"""module documentation"""

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

    Rows = cur.fetchall()

    for row in Rows:
        print(*row, sep=': ')

    con.close()
