#!/usr/bin/python3

"""Module Documentation"""
import sys
import MySQLdb

if __name__ == "__main__":
    con = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3],
                          port=3306, host='localhost')

    curse = con.cursor()

    curse.execute("""SELECT cities.name AS city_name
                         FROM cities
                         JOIN states ON cities.state_id = states.id
                         WHERE states.name = '{}%'
                         ORDER BY cities.id ASC""".format(sys.argv[4]))

    rows = curse.fetchall()

    for row in rows:
        print("{}, ".format(row), end="")

    con.close()
