#!/usr/bin/env python3

import sounddevice as sd
import soundfile as sf
from tkinter import *
import datetime
import pyfiglet


result = pyfiglet.figlet_format("Soundrecorder")
print(result)
print("\n") # describtion-row
os.system("date")
print("-----------------------------------------")


def Voice_rec():
    fs = 48000

    duration = 5
    myrecording = sd.write('my_Audio.flac', myrecording, fs)

master = Tk()

Label(master, text=" Sound Recorder : ").grid(row=0, sticky=W, rowspan=5)



b = Button(master, text="Start", command=Voice_rec)
b.grid(row=0, column=2, columnspan=2, rowspan=2, padx=5, pady=5)

mainloop()
