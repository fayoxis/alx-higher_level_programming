#!/usr/bin/python3
""" Object-relational mapping """


if __name__ == '__main__':
    import sys
    import MySQLdb

    if len(sys.argv) != 4:
        sys.exit('Use: 0-select_states.py <mysql username> <mysql password>'
                 ' <database name>')

    conn = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], charset='utf8')
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = list(cur)
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
