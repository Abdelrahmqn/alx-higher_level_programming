#!/usr/bin/python3

"""Write a script that takes in an argument
and displays all values in the states"""

import sys
import MySQLdb

if __name__ == "__main__":
    con = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                          db=sys.argv[3], port=3306, host='localhost')

    curse = con.cursor()

    curse.execute("""SELECT id, name FROM states WHERE name LIKE '{}%'
                    ORDER BY states.id ASC""".format(sys.argv[4]))

    rows = curse.fetchall()

    for row in rows:
        print(row)

    con.close()
