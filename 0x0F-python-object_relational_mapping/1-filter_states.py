#!/usr/bin/python3
"""filters all states starting with 'N' """
from sys import argv
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         password=argv[2],
                         database=argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM `states` ORDER BY `id`")
    [print(state) for state in cursor.fetchall() if state[1][0] == "N"]
