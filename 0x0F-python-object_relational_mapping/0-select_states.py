#!/usr/bin/python3

"""Module Documentaion"""


import sys
import MySQLdb


if __name__ == "__main__":
        conn = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                               db=sys.argv[3], port=3306,
                               host="localhost")

        cursor = conn.cursor()
        cursor.execute("SELECT id, name FROM states ORDER BY id ASC")

        result = cursor.fetchall()

        for row in result:
                print(row)

        conn.close()
        cursor.close()
