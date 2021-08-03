#!/usr/bin/env python3

import os
import random
import smtplib


def automatic_email():
    user = input(" name >>: ")
    email = input(" email ID>>: ")


    s = smtplib.SMTP('smtp.gmail.com', #PORT)
    s.starttls()
    s.login("Your Gmail Account", "PW ")
    s.sendmail('&&&&&&&&&&&', email, message)
    print("Email Sent!")
    
automatic_email()
