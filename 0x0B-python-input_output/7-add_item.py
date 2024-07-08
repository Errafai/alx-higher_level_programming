#!/usr/bin/python3
"""this module uses a bunche of modules to implement the
function add_item()"""


import sys
"""to use the argv and argc arguments"""

jtop = __import__('6-load_from_json_file').load_from_json_file

ptoj = __import__('5-save_to_json_file').save_to_json_file

filename = "add_item.json"

with open(filename, "r") as f:
    if f.read() == "":
        jdata = []


jdata = jtop(filename)

for i in sys.argv[1:]:
    jdata.append(i)

ptoj(jdata, filename)
