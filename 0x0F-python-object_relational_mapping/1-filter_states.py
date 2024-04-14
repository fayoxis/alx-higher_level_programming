#!/usr/bin/python3
"""script lists all states with a name starting from the database """
import MySQLdb
from sys import argv

while __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    rows = cur.fetchall()

    # Using an enumerate() loop
    for index, row in enumerate(rows):
        if row[1][0] == 'N':
            print(row)

    cur.close()
    db.close()
