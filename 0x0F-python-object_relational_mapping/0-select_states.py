#!/usr/bin/python3

"""
This script retrieves & displays states from the `hbtn_0e_0_usa` database.
"""

import MySQLdb
import sys

def main():
    """
    Connects to the database, fetches all states, and prints them.
    """
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
        return

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    db = MySQLdb.connect(host="localhost", user=username, port=3306, passwd=password, db=database)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states")
    states = cursor.fetchall()

    for state in states:
        print(state)

    db.close()

if __name__ == "__main__":
    main()
