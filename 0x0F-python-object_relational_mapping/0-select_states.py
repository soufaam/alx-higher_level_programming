#!/usr/bin/python3
"""A python3  script that lists all states from the
database hbtn_0e_0_usa"""

import MySQLdb
import sys

"""connect to the MYSQL SERVER"""
db = MySQLdb.connect(host='127.0.0.1', port=13306,
                     user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
cur = db.cursor()
command_sql = 'SELECT * FROM states ORDER BY states.id'
result = cur.execute(command_sql)
for row in cur.fetchall():
    print(row)
