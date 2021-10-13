#!/usr/bin/env python3


import string
from random import *
import pyfiglet


result = pyfiglet.figlet_format("Password:")
print(result)
print("----------------------------------------------")

letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation
chars = letters + digits + symbols

min_lenght = 13
max_lenght = 19

password = "".join(choice(chars) for x in 
range(randint(min_lenght, max_lenght)))

print(password)
print("----------------------------------------------")
