#!/usr/bin/python3
"""
Takes in the name of a state as an argument and lists all `cities`
of that `state`, using the database `hbtn_0e_4_usa`
The code is safe from MySQL injections.
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])
    cursor = db.cursor()
    searched = argv[4]
    cursor.execute("SELECT cities.name FROM cities JOIN states \
                    ON states.id = cities.state_id AND states.name LIKE %s \
                    ORDER BY cities.id", (searched,))
    selected = cursor.fetchall()

    for record in selected:
        print(record)

    cursor.close()
    db.close()
