#!/usr/bin/python3

"""
This module lists all states from the database
The script will take 3 arguements: my sql username, mysql password
and database name.
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
    cursor.execute("SELECT * FROM states\
            WHERE name LIKE BINARY 'N%' ORDER BY states.id ASC")
    states = (cursor.fetchall())
    for state in states:
        print(state)
    cursor.close()
