#!/usr/bin/python3
"""lists cities by states"""
import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT `c`.`id`, `c`.`name`, `s`.`name` \
                     FROM `cities` as `c` \
                    INNER JOIN `states` as `s` \
                       ON `c`.`state_id` = `s`.`id` \
                    ORDER BY `c`.`id`")
    [print(city) for city in cursor.fetchall()]
