#!/usr/bin/python3

"""
This module lists all states from the database
The script will take 3 arguements: my sql username, mysql password
and database with name starting with N.
"""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name\
            FROM cities LEFT OUTER JOIN states\
            ON states.id = cities.state_id\
            ORDER BY cities.id ASC")
    states = (cursor.fetchall())
    for state in states:
        print(state)
    cursor.close()
