#!/usr/bin/python3
"""Script  takes the name of state in an argument and lists
all cities """
import mysql.connector
from sys import argv

if __name__ == "__main__":
    # Connect to the MySQL database
    db = mysql.connector.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        password=argv[2],
        database=argv[3],
        charset="utf8"
    )

    # Create a cursor object
    cursor = db.cursor()

    # Execute the SQL query
    cursor.execute(
        "SELECT cities.name "
        "FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "WHERE states.name LIKE %s "
        "ORDER BY cities.id",
        (argv[4],)
    )

    # Fetch the results and print them
    rows = cursor.fetchall()
    print(", ".join(city[0] for city in rows))

    # Close the cursor and the database connection
    cursor.close()
    db.close()
