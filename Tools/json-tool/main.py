#!/usr/bin/env python3


import json


# read a JSON file
# 1st option
file_name = "xy.json"
with open(file_name) as f:
    data = json.load(f)
    
print(data)
# 2nd option
file_name = "xy.json"
with open(file_name) as f:
    data = json.loads(f.read())

print(data)


# MAKE read.py , write.py 
