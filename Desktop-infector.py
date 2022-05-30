from ntpath import join
import os
import hashlib
from pystyle import *
from random import *
desktop = os.path.join(os.path.expanduser("~"), "Desktop")

YOUR_TXT = "ENTER YOUR TEXT HERE"

for x in range(10):
    myfoldername = hashlib.sha256(("Random" + str(randint(1,1000000))).encode()).hexdigest()
    efolder      = os.path.join(desktop, myfoldername)
    os.mkdir(efolder)
    Write.Print(f"[Dir] --> {efolder}\n", Colors.green, interval=0)
    for f in range(100):
        myfilename = hashlib.sha256(("File Infected: " + str(randint(1,1000000))).encode()).hexdigest() + ".txt"
        with open(efolder + "\\" + myfilename, 'w') as file:
            for w in range(10000):
               file.write(YOUR_TXT)
