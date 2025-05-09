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

    query = "SELECT * FROM states WHERE name = '{}'".format(str(ar[4]))
    cursor.execute(query)

    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    connector.close()
