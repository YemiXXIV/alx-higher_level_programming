#!/usr/bin/python3
"""List all states with names from argument
from database hbtn_0e_0_usa safe from MySQL injections
"""
import MySQLdb
import sys


def main():
    """List all states with names from argument
    from database hbnt_0e_0_usa safe from MySQL injections
    """
    HOST = 'localhost'
    PORT = 3306
    USERNAME = sys.argv[1]
    PASSWORD = sys.argv[2]
    DATABASE = sys.argv[3]
    ARGUMENT = sys.argv[4]
    db = MySQLdb.connect(
            host=HOST,
            port=PORT,
            user=USERNAME,
            passwd=PASSWORD,
            db=DATABASE
    )
    cur = db.cursor()
    firstQuery = """SELECT id, name FROM states WHERE name """
    secondQuery = """= %s ORDER BY id ASC"""
    finalQuery = firstQuery + secondQuery
    cur.execute(finalQuery, (ARGUMENT,))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    main()
