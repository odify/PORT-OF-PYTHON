#!/usr/bin/env python3

import requests
import re

url = input('YOUR URL (include `http://`): ')

website = requests.get(url)

html = website.text
links = re.findall('"((http|ftp)s?://.*?)"', html)
emails = re.findall('([\w\.,]+@[\w\.,]+\.\w+)', html)

print("\nFound {} links".format(len(links)))
for email in emails:
    print(email)


