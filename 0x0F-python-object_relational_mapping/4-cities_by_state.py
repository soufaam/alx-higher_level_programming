#!/usr/bin/python3
"""A python3  script that lists all states from the
database hbtn_0e_0_usa"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    """connect to the MYSQL SERVER"""
    db = MySQLdb.connect(host='127.0.0.1', port=13306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    command_sql = "SELECT cities.id, cities.name, states.name  FROM cities \
    LEFT JOIN states ON cities.state_id = states.id"
    result = cur.execute(command_sql)
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()
