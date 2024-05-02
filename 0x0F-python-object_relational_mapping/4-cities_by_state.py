#!/usr/bin/python3
"""List all cities from database hbtn_0e_4_usa
"""
import MySQLdb
import sys


def main():
    """List all cities from database hbnt_0e_4_usa
    """
    HOST = 'localhost'
    PORT = 3306
    USERNAME = sys.argv[1]
    PASSWORD = sys.argv[2]
    DATABASE = sys.argv[3]
    db = MySQLdb.connect(
            host=HOST,
            port=PORT,
            user=USERNAME,
            passwd=PASSWORD,
            db=DATABASE
    )
    cur = db.cursor()
    firstQ = "SELECT cities.id, cities.name, states.name FROM cities "
    secQ = "JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC"
    finQ = firstQ + secQ
    cur.execute(finQ)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    main()
