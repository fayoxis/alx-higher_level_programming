#!/usr/bin/python3
"""Script  takes the name of state in an argument and lists
all cities """
import MySQLdb
from sys import argv

if __name__ == "__main__":
    # Connect to the MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        charset="utf8"
    )

    # Create a cursor object
    cur = db.cursor()

    # Execute the SQL query
    cur.execute(
        "SELECT cities.name "
        "FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "WHERE states.name LIKE %s "
        "ORDER BY cities.id",
        (argv[4],)
    )

    # Fetch the results and print them
    rows = cur.fetchall()
    print(", ".join(city[0] for city in rows))

    # Close the cursor and the database connection
    cur.close()
    db.close()
