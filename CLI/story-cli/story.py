#!/usr/bin/env python3


from random import choice
import pyfiglet

result = pyfiglet.figlet_format("Story generator")
print(result)
# print("\n") # describtion-row
print("------------------------------------")

def story_gen():

    wer = ['Ferdi', 'Rene', 'Malina', 'Sarah']
    was = ['aß Obstsalat mit Stäbchen', 'flog nach China', 'kam zu spät zum Treffpunkt', 'musste sich übergeben']
    wann = ['vor ein paar Tagen', 'gestern', 'grade eben', 'vorgestern']
    action = ['aber leider regnete es mal wieder', 'und wurde somit zum Held des Tages', 'wahrscheinlich unter größter Anstrengung', 'und war total in partylaune']



    return print(choice(wer) + ' ' + choice(was) + ' ' + choice(wann) + ' ' + choice(action))

def print_story():
    story_gen()
    print('------------------------------------')

if __name__ == '__main__':
    print_story()
