#!/usr/bin/python3

""""Module Documentation"""
import sys
import MySQLdb

if __name__ == "__main__":
    conn = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                           db=sys.argv[3], port=3306, host='localhost')

    curse = conn.cursor()

    curse.execute("""SELECT * FROM states WHERE name
                LIKE 'N%' ORDER BY states.id ASC""")

    result = curse.fetchall()

    for row in result:
        print(row)

    conn.close()
    curse.close()
