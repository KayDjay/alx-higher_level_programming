#!/usr/bin/python3

""" The module lists all states from the database hbtn_0e_0_usa """

from sys import argv
import MySQLdb

if __name__ == "__main__":

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )
    cursor = db.cursor()
    query = "SELECT GROUP_CONCAT(name ORDER BY id ASC SEPARATOR ', ') \
        FROM cities WHERE state_id = \
        (SELECT id FROM states WHERE name = %s)"
    cursor.execute(query, (argv[4],))
    states = cursor.fetchall()
    for state in states:
        for i in state:
            if i:
                print(i)
    cursor.close()
