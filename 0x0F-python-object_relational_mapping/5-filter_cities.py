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
                         WHERE states.name = %s
                         ORDER BY cities.id ASC""", (sys.argv[4],))

    rows = curse.fetchall()

    step = list(row[0] for row in rows)
    print(*step, sep=", ")

    con.close()
