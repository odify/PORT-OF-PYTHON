#!/usr/bin/env python3  


import os
import datetime
import time
import progressbar
from progress.bar import IncrementalBarimport time
from progress.bar import IncrementalBar

print("-------------------------------------")

print("_____________________________________")
print("\n")
print("\n")


mylist = [1,2,3,4,5,6,7,8,9]
bar = IncrementalBar('Countdown', max = len(mylist))
for item in mylist:
    bar.next()
    time.sleep(1)
bar.finish()


#bar = IncrementalBar('Countdown', max = len(mylist))
#for item in mylist:
#    bar.next()
#    time.sleep(1)
# bar.finish()

#def animated_marker():
#    widgets = ['Loading: ', progressbar.AnimatedMarker()]
#    bar = progressbar.ProgressBar(widgets=widgets).start()
#    for i in range(43):
#        time.sleep(0.13)
#        bar.update(i)
#animated_marker()

#widgets = [' [',
#         progressbar.Timer(format= 'elapsed time: %(elapsed)s'),
#         '] ',
#         progressbar.Bar('*'),' (',
#       progressbar.ETA(), ') ',
#     ]
#bar = progressbar.ProgressBar(max_value=200, 
#                              widgets=widgets).start()
#for i in range(200):
#    time.sleep(0.1)
#   bar.update(i)





os.system("date")
print("\n")

print("-------------------------------------")

print("\n")
print("\n")



