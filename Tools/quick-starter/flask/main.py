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
pyautogui.typewrite('create-flask-app ' + project)
pyautogui.typewrite(['enter'])
pyautogui.typewrite(['flaskproject'])
# pyautogui.typewrite('cd ' + project + ' &&' + ' python3 manage.py startapp ' + new)
pyautogui.typewrite(['enter'])

pyautogui.typewrite(['space'])
pyautogui.typewrite(['enter'])



time.sleep(1)

pyautogui.typewrite(['down'])
pyautogui.typewrite(['down'])
pyautogui.typewrite(['space'])
pyautogui.typewrite(['down'])
pyautogui.typewrite(['down'])
pyautogui.typewrite(['down'])
pyautogui.typewrite(['down'])
pyautogui.typewrite(['down'])
pyautogui.typewrite(['down'])
pyautogui.typewrite(['down'])
pyautogui.typewrite(['down'])
pyautogui.typewrite(['space'])
pyautogui.typewrite(['down'])
pyautogui.typewrite(['down'])
pyautogui.typewrite(['space'])


# pyautogui.typewrite('python3 manage.py migrate')
# pyautogui.typewrite(['enter'])
# pyautogui.typewrite('python3 manage.py runserver')
# pyautogui.typewrite(['enter'])
