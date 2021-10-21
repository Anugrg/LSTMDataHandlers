import json
import os
import glob


os.chdir("/home/anubinda/Data/")
fil = open(r"list.txt","w")

for file in glob.glob("*.json"):
    fil.write(fname + "\n")

fil.close()



