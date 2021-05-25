#!/usr/bin/env python3


import pyautogui
import time



terminal = ''
dir = ''
folder = ''
project = 'test'
new = 'app'



pyautogui.press('win')
pyautogui.typewrite(terminal)
pyautogui.typewrite(['enter'])
pyautogui.typewrite('cd ./' + dir + ' &&' + ' mkdir ' + folder + ' && ' + 'cd ' + folder)
pyautogui.typewrite(['enter'])
pyautogui.typewrite('django-admin.py startproject ' + project)
pyautogui.typewrite(['enter'])
pyautogui.typewrite('cd ' + project + ' &&' + ' python3 manage.py startapp ' + new)
pyautogui.typewrite(['enter'])

time.sleep(1)

pyautogui.typewrite('python3 manage.py migrate')
pyautogui.typewrite(['enter'])
pyautogui.typewrite('python3 manage.py runserver')
pyautogui.typewrite(['enter'])
