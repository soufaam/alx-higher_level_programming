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
    param = sys.argv[4]
    command_sql = "SELECT cities.name  FROM cities \
    LEFT JOIN states ON cities.state_id = states.id \
 WHERE states.name = %(param)s\
 ORDER BY cities.id ASC"
    result = cur.execute(command_sql, {'param': param})
    rows = cur.fetchall()
    length_rows = len(rows)
    for idx in range(length_rows):
        if rows[idx] != rows[length_rows - 1]:
            print(rows[idx][0], end=', ')
        else:
            print(rows[idx][0], end='')
    print()
    cur.close()
    db.close()
