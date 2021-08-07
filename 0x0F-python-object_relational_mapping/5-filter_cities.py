#!/usr/bin/python3
""" takes state as an arguement and lists all cities of that state"""
import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM `cities` as `c` \
                     INNER JOIN `states` as `s` \
                        ON `c`.`state_id` = `s`.`id` \
                    ORDER BY `c`.`id`")
    fetch = cursor.fetchall()
    print(", ".join([ct[2] for ct in fetch if ct[4] == sys.argv[4]]))
