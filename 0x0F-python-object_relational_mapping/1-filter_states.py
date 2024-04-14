#!/usr/bin/python3
#!/usr/bin/python3
"""script lists all states with a name starting from
the database """


import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    rows = cur.fetchall()

    # Using a for loop
    for row in rows:
        if row[1][0] == 'N':
            print(row)

    # Using a while loop
    i = 0
    while i < len(rows):
        if rows[i][1][0] == 'N':
            print(rows[i])
        i += 1

    cur.close()
    db.close()
