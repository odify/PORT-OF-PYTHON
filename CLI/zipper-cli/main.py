#!/usr/bin/env python3

import os
from zipfile import ZipFile
import datetime
import pyfiglet


result = pyfiglet.figlet_format("Zipper CLI")
print(result)
os.system("date")
print("-------------------------------------")


def zip_me(path):
    """ Your folder path & name """
    folder_name = path.split("\\")[-1]
    rel_path = path.strip(folder_name)

    """ Save to the target folder path """
    os.chdir(rel_path)

    parse = ZipFile(f"{folder_name}.zip", "w")


    for root, dirs, files in os.walk(folder_name, topdown=False):
        """ Files in sub-folders """
        for name in files:
            file = os.path.join(root, name)
            parse.write(file)

        """ Sub-folders in target folder """
        for name in dirs:
            folders = os.path.join(root, name)
            parse.write(folders)
    parse.close()
        

if __name__ == "__main__":
    path = input(r"Path to target folder: ")
    zip_me(path)
