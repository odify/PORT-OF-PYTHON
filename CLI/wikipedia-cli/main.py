#!/usr/bin/env python3



import wikipedia
import os
import datetime
import pyfiglet


result = pyfiglet.figlet_format("Wikipedia cli")
print(result)
# print("\n") # describtion-row
os.system("date")
print("------------------------------------")

def searcher(question):
    answer = wikipedia.summary(question).split(".")
    for line in answer:
        print(line)

if __name__ == "__main__":
    question = input("Search now: ")
    searcher(question)


