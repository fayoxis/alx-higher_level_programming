#!/usr/bin/python3
"""Script  takes the name of state in an argument and lists
all cities """
import MySQLdb
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    with db.cursor() as cur:
        cur.execute("""
            SELECT
                cities.name
            FROM
                cities
            JOIN
                states
            ON
                cities.state_id = states.id
            WHERE
                states.name = %s
            ORDER BY
                cities.id ASC
        """, (argv[4],))

        rows = cur.fetchall()

     if rows is not None:
        print(", ".join(row[0] for row in rows))
