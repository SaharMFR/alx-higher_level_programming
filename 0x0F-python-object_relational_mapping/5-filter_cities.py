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
    cursor.execute("SELECT cities.name FROM cities INNER JOIN states \
                    ON states.id = cities.state_id WHERE \
                    states.name =  %s", (searched,))
    selected = cursor.fetchall()

    temp_list = list(record[0] for record in selected)
    print(*temp_list, sep=", ")

    cursor.close()
    db.close()
