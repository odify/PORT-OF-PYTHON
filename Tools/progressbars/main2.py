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
animation = [
"[        ]",
"[=       ]",
"[===     ]",
"[====    ]",
"[=====   ]",
"[======  ]",
"[======= ]",
"[========]",
"[ =======]",
"[  ======]",
"[   =====]",
"[    ====]",
"[     ===]",
"[      ==]",
"[       =]",
"[        ]",
"[        ]"
]

notcomplete = True

i = 0

while notcomplete:
    print(animation[i % len(animation)], end='\r')
    time.sleep(.1)
    i += 1
