#!/usr/bin/python3
"""
List all states with names starting with N
from database hbtn_0e_0_usa
"""
import MySQLdb
import sys


def main():
    """
    List of all states with names starting with N
    from database
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
    f_Query = "SELECT id, name FROM states WHERE name "
    s_Query = "LIKE BINARY 'N%' ORDER BY id ASC"
    finalQuery = f_Query + s_Query
    cur.execute(finalQuery)
    result = cur.fetchall()
    for row in result:
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    main()
