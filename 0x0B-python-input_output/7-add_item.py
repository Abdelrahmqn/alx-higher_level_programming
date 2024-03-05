#!/usr/bin/python3
"""Write a script that adds all arguments to a Python list
"""

import sys
import json
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


filen="add_item.json"
lst=[]
lst.append(sys.argv[1:])
save_to_json_file(lst, filen)
load_from_json_file(filen)
