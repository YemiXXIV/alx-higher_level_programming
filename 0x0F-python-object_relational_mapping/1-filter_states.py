#!/usr/bin/python3
"""
List all states with names starting with N
from database hbtn_0e_0_usa
"""
import MySQLdb
import sys


def main():
    """
    List all states with names starting with N
    from database hbnt_0e_0_usa
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
    cursor = db.cursor()
    firstQuery = "SELECT id, name FROM states WHERE name"
    secondQuery = "LIKE BINARY 'N%' ORDER BY id ASC"
    finalQuery = firstQuery + secondQuery
    cursor.execute(finalQuery)
    result = cursor.fetchall()
    for row in result:
        print(row)
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
