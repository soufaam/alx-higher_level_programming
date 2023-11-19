#!/usr/bin/python3
"""A python3  script that lists all states from the
database hbtn_0e_0_usa"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    """connect to the MYSQL SERVER"""
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], charset="utf8")
    cur = db.cursor()
    command_sql = "SELECT * FROM states WHERE states.name LIKE BINARY '{}' \
ORDER BY states.id ASC;".format(sys.argv[4])
    result = cur.execute(command_sql)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
