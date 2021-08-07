#!/usr/bin/python3
""" takes an arguement and displays all states that match the arguement """
import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * \
                      FROM `states` \
                      WHERE BINARY `name` = '{}'".format(sys.argv[4]))
    [print(state) for state in cursor.fetchall()]
