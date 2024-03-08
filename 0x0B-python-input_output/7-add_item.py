#!/usr/bin/python3
"""Write a script that adds all arguments to a Python list
"""

from os import path
import sys
import json
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


filen = "add_item.json"
if not path.exists(filen):
    open(filen, 'w').close()

try:
    lst = load_from_json_file(filen)
except FileNotFoundError:
    lst = []
for arg in sys.append[1:]:
    lst.append(arg)

save_to_json_file(lst, filen)
load_from_json_file(filen)
