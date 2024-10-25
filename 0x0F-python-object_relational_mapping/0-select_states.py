#!/usr/bin/python3
"""this module connect the hbtn_0e_0_usa module and select all data
in the satates table """


import MySQLdb
import sys


ar = sys.argv

connector = MySQLdb.connect(host="localhost", user=ar[1], passwd=ar[2],
                            port=3306, db=ar[3]
                            )
cursor = connector.cursor()

cursor.execute("SELECT * FROM states")

states = cursor.fetchall()

for state in states:
    print(state)
