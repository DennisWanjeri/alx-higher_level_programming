#!/usr/bin/python3
""" displays all contents of states table
 with protection from SQL injection """
import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM `states`")
    fetch = cursor.fetchall()
    [print(state) for state in fetch if state[1] == sys.argv[4]]
