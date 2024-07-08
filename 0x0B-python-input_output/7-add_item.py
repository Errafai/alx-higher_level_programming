#!/usr/bin/python3
"""this module uses a bunche of modules to implement the add_item"""


import sys
"""to use the argv and argc arguments"""

load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

filename = "add_item.json"

try:
    jdata = load_from_json_file(filename)
except Exception:
    jdata = []

for i in sys.argv[1:]:
    jdata.append(i)

save_to_json_file(jdata, filename)
