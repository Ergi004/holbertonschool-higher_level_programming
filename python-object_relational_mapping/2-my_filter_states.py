#!/usr/bin/python3
"""
Write a script that takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument.
"""


import MySQLdb
import sys

def get_states(username, password, db_name, state_name):
    db = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        db=db_name,
        port=3306
    )

    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()

if __name__ == "__main__":
    get_states(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])

