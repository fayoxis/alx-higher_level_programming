#!/usr/bin/python3
import MySQLdb
from sys import argv

if __name__ == "__main__":
    # Connect to the database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        charset="utf8"
    )

    # Create a cursor
    with db.cursor() as cur:
        # Execute the query to select all states
        cur.execute("SELECT * FROM states ORDER BY id ASC")

        # Fetch all the rows and print them
        for row in cur.fetchall():
            print(row)
