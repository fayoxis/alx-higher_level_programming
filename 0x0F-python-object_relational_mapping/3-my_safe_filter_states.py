#!/usr/bin/python3
"""Script that takes in arguments and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument, safe from MySQL
injections"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])
    with db.cursor() as cur:
        cur.execute("""
            SELECT
                *
            FROM
                states
            WHERE
                name LIKE BINARY %(name)s
            ORDER BY
                states.id ASC
        """, {
            'name': argv[4]
        })

        rows = cur.fetchall()

    if rows:
        for row in rows:
            print(row)
