#!/usr/bin/env python3


import json

x = {
  "name": "ferdi",
  "age": 29,
  "city": "Langenfeld"
}


#Convert into JSON

y = json.dumps(x)

#JSON CREATED

print(y)
