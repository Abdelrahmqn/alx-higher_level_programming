#!/usr/bin/python3

"""Module Documentation"""
import sys
import MySQLdb

if __name__ == "__main__":
    con = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3],
                          port=3306, host='localhost')

    curse = con.cursor()

    curse.execute("""SELECT cities.id, cities.name AS city_name, states.name AS
                     state_name
                     FROM cities
                     JOIN states ON cities.state_id = states.id
                     ORDER BY cities.id ASC""")

    rows = curse.fetchall()

    for row in rows:
        print(row)

    con.close()
