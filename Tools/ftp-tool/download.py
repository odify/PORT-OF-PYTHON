#!/usr/bin/env python3


# DOWNLOAD "myfile.txt"

import ftplib


FTP_HOST = " YOUR FTP HOSTNAME "
FTP_USER = " YOUR FTP USERNAME "
FTP_PASS = " PASSWORD "


ftp = ftplib.FTP(FTP_HOST, FTP_USER, FTP_PASS)
ftp.encoding = "utf-8"


filename = "myfile.txt"
with open(filename, "wb") as file:

ftp.retrbinary(f"RETR {filename}", file.write)


ftp.quit()
