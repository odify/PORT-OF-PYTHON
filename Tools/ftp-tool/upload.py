#!/usr/bin/env python3


# UPLOAD "myfile.txt"

import ftplib


FTP_HOST = " YOUR FTP HOSTNAME "
FTP_USER = " YOUR FTP USERNAME "
FTP_PASS = " PASSWORD "


ftp = ftplib.FTP(FTP_HOST, FTP_USER, FTP_PASS)
ftp.encoding = "utf-8"


filename = "myfile.txt"
with open(filename, "rb") as file:

ftp.storbinary(f"STOR {filename}", file)

ftp.dir()

ftp.quit()
