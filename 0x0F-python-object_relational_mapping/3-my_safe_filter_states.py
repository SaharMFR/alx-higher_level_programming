#!/usr/bin/python3
"""
Takes in an argument and displays all values in the `states` table
of `hbtn_0e_0_usa` where `name` matches the argument.
The code is safe from MySQL injections.
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])
    cursor = db.cursor()
    searched = argv[4]
    cursor.execute("SELECT * FROM states WHERE name LIKE %s \
                    ORDER BY states.id", (searched,))
    selected = cursor.fetchall()

    for record in selected:
        print(record)

    cursor.close()
    db.close()
