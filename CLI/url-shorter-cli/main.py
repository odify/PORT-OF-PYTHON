#!/usr/bin/env python3

import pyshorteners
import os
import datetime
import pyfiglet


result = pyfiglet.figlet_format("URL Shorter")
print(result)
os.system("date")
print("\n") # describtion-row



url = input("Enter URL")

s = pyshorteners.Shortener().tinyurl.short(url)
print("Shorted URL -->", s)
