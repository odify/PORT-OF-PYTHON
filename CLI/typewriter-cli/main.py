#!/usr/bin/env python3


import pyfiglet
import pyautogui



result = pyfiglet.figlet_format("TYPEWRITER")
print(result)

print("-------------------------------------")
print("-------------------------------------")


pyautogui.typewrite('Hello world of python', interval=0.19 )

pyautogui.typewrite('...................', interval=0.08 )

pyautogui.typewrite('„Lorem ipsum dolor sit amet, consectetur adipisici elit, …" ist ein Blindtext, der nichts bedeuten soll, sondern als Platzhalter im Layout verwendet wird, um einen Eindruck vom fertigen Dokument zu erhalten. ', interval=0.33 )

pyautogui.typewrite('Die Verteilung der Buchstaben und der Wortlängen des pseudo-lateinischen Textes entspricht in etwa der natürlichen lateinischen Sprache. Der Text ist absichtlich unverständlich, damit der Betrachter nicht durch den Inhalt abgelenkt wird.', interval=0.5 )

pyautogui.typewrite('Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet', interval=0.83 )

print("-------------------------------------")
