#!/usr/bin/python3
"""List all cities with state name from argument
from database hbtn_0e_0_usa safe from MySQL injections
"""
import MySQLdb
import sys


def main():
    """List all cities with state name from argument
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
    firstQ = "SELECT cities.name FROM cities JOIN states ON cities.state_id"
    secQ = "= states.id WHERE states.name = %s ORDER BY cities.id ASC"
    finalQuery = firstQ + secQ
    cur.execute(finalQuery, (ARGUMENT,))
    rows = cur.fetchall()
    cities = []
    for row in rows:
        for col in row:
            cities.append(col)
    cityList = ', '.join(cities)
    print(cityList)
    cur.close()
    db.close()


if __name__ == "__main__":
    main()
