#!/usr/bin/python3
"""Script lists all cities from the database """
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities \
    JOIN states ON cities.state_id = states.id ORDER BY cities.id")
    
    # Fetch all the rows
    rows = cur.fetchall()
    
    # Iterate over the rows and print each one in a formatted way
    for city_id, city_name, state_name in rows:
        print(f"City ID: {city_id}, City Name: {city_name}, State Name: {state_name}")
    
    cur.close()
    db.close()
