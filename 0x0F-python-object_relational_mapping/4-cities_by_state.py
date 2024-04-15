#!/usr/bin/python3

"""Module Documentation"""
import sys
import MySQLdb

if __name__ == "__main__":
    con = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3],
                          port=3306, host='localhost')

    curse = con.cursor()

    curse.execute("""SELECT id, name FROM cities
                     ORDER BY cities.id ASC""")

    rows = curse.fetchall()

    for row in rows:
        print(row)

    con.close()
