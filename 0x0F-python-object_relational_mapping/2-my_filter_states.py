#!/usr/bin/python3
"""
Script that displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.
"""
import MySQLdb
import sys


def main():
    """
    Main function
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
    f_Query = "SELECT id, name FROM states WHERE name "
    s_Query = "LIKE BINARY '{}' ORDER BY id ASC".format(ARGUMENT)
    finalQuery = f_Query + s_Query
    cur.execute(finalQuery)
    results = cur.fetchall()
    for row in results:
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    main()
