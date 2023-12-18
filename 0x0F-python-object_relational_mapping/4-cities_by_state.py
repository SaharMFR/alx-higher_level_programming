#!/usr/bin/python3
"""
Takes in an argument and displays all values in the `cities` table
of `hbtn_0e_4_usa` where `name` matches the argument.
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name \
                    FROM cities JOIN states ON states.id = cities.state_id")
    selected = cursor.fetchall()

    for record in selected:
        print(record)

    cursor.close()
    db.close()
