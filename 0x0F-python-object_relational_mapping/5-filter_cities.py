#!/usr/bin/python3
"""this module connect the hbtn_0e_0_usa module and select all data
in the satates table """


import MySQLdb
import sys

if __name__ == "__main__":
    ar = sys.argv

    connector = MySQLdb.connect(host="localhost", user=ar[1], passwd=ar[2],
                                port=3306, db=ar[3]
                                )
    cursor = connector.cursor()

    query = """SELECT DISTINCT cities.name FROM cities
            INNER JOIN states ON cities.state_id = states.id
            WHERE states.name = %s"""
    cursor.execute(query, (ar[4],))

    states = cursor.fetchall()
    to_list = [cities[0] for cities in states]
    print(", ".join(to_list))

    cursor.close()
    connector.close()
