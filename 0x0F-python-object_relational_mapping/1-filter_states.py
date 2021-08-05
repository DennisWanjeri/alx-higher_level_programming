#!/usr/bin/python3
# filters all states starting with 'N'
import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM `states` ORDER BY `id`")
    [print(state) for state in cursor.fetchall() if state[1][0] == "N"]
