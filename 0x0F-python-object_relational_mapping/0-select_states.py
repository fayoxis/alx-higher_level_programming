#!/usr/bin/python3

if __name__ == '__main__':
    import sys
    import mysql.connector

    if len(sys.argv) != 4:
        sys.exit('Usage: python 0-select_states.py <mysql username> <mysql password> <database name>')

    try:
        conn = mysql.connector.connect(
            host='localhost',
            port=3306,
            user=sys.argv[1],
            password=sys.argv[2],
            database=sys.argv[3],
            charset='utf8'
        )
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM states ORDER BY id ASC")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        cursor.close()
        conn.close()
    except mysql.connector.Error as err:
        sys.exit(f"Error connecting to the database: {err}")
