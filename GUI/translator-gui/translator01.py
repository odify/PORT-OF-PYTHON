#!/usr/bin/env python3


from tkinter import *
import tkinter as tk
from tkinter import ttk
from googletrans import Translator
from tkinter import messagebox

root = tk.Tk()
root.title(' Translator V 0.1 ')

root.geometry('550x450')

root.maxsize(1400,900)

root.minsize(410,530)


def translate():
        language_1 = t1.get("1.0","end-1c")
        cl = choose_langauge.get()

        if language_1 == '':
                messagebox.showerror('INPUT')
        else:
                translator = Translator()
                output = translator.translate(language_1, dest=cl)
                t2.insert('end',output.text)

def clear():

        t1.delete(1.0,'end')
        t2.delete(1.0,'end')
        


a = tk.StringVar() 
auto_detect = ttk.Combobox(root, width = 30, textvariable = a, state='readonly',font=('verdana',11,'bold'),)


auto_detect['values'] = (
                          'German',

'Odia',
'Hebrew',
'English',
'Persian',
'Polish',
'Russian',
'Dutch',
'Auto Detect',
                          ) 
  
auto_detect.place(x=30,y=70)
auto_detect.current(0) 

l = tk.StringVar() 
choose_langauge = ttk.Combobox(root, width = 30, textvariable = l, state='readonly',font=('verdana',11)) 
  

# TRANSLATIONS ARRAY

choose_langauge['values'] = (
                        'Hebrew',
                        'Afrikaans',
                        'Albanian',
                        'Arabic',
                        'Armenian',
                       ' Azerbaijani',
                        'Basque',
                        'Belarusian',
                        'Bengali',
                        'Bosnian',
                        'Bulgarian',
                        'Cebuano',
                        'Chichewa',
                        'Chinese',
                        'Corsican',
                        'Croatian',
                       ' Czech',
                        'Danish',
                        'Dutch',
                        'English',
                        'Esperanto',
                        'Estonian',
                        'Finnish',
                        'French',
                        'Frisian',
                        'Georgian',
                        'German',
                        'Greek',
                        'Gujarati',
                        'Hausa',
                        'Hindi',
                        'Hungarian',
                        'Indonesian',
                        'Irish',
                        'Italian',
                        'Japanese',
                        'Javanese',
                        'Kazakh',
                        'Khmer',
                        'Kinyarwanda',
                        'Korean',
                        'Kurdish',
                        'Latin',
                        'Latvian',
                        'Lithuanian',
                        'Macedonian',
                        'Malagasy',
                        'Malay',
                        'Malayalam',
                        'Maltese',
                        'Maori',
                        'Marathi',
                        'Mongolian',
                        'Myanmar',
                        'Nepali',
                        'Norwegian'
                        'Odia',
                        'Pashto',
                        'Persian',
                        'Polish',
                        'Portuguese',
                        'Punjabi',
                        'Romanian',
                        'Russian',
                        'Samoan',
                        'Scots Gaelic',
                        'Serbian',
                        'Sesotho',
                        'Shona',
                        'Sindhi',
                        'Slovak',
                        'Slovenian',
                        'Somali',
                        'Spanish',
                        'Sundanese',
                        'Swahili',
                        'Swedish',
                        'Tajik',
                        'Tamil',
                        'Tatar',
                        'Telugu',
                        'Thai',
                        'Turkish',
                        'Turkmen',
                        'Urdu',
                        'Uzbek',
                        'Vietnamese',
                        'Welsh',
                        'Yiddish',
                        'Yoruba',
                        'Zulu',
                          ) 


choose_langauge.place(x=290,y=70)
choose_langauge.current(0) 


t1 = Text(root,width=30,height=7,borderwidth=4,relief=RIDGE)
t1.place(x=10,y=100)

t2 = Text(root,width=30,height=7,borderwidth=4,relief=RIDGE)
t2.place(x=260,y=100)


button = Button(root,text="TRANSLATE",relief=RIDGE,borderwidth=3,font=('verdana',11),cursor="hand2",command=translate)

button.place(x=280,y=280)


clear = Button(root,text="RESET",relief=RIDGE,borderwidth=3,font=('verdana',14,'bold'),cursor="hand2",command=clear)
clear.place(x=80,y=280)


root.mainloop()


