import pandas as pd
import glob
import os
import shutil
import re
from pathlib import Path


def copyFile(src,dest):
    shutil.copy(src,dest)


print("starting....")

destination = Path.home() / "dataset" / "point"
print(destination)
for subdir, dirs, files in os.walk("/home/anubinda/new_skeleton_dataset/datasets_normal/"):
    for file in files:
        if re.search("point",file):
            dir = subdir
            print(dir)
            #path = os.path.join(destination,dir)
            #if not os.path.exists(path):
            #    os.mkdir(path)
            #print("file => " + path)
            copy_this = subdir + "/" + file
            
            copyFile(copy_this, destination )
            print("moved => " + copy_this)


print("completed...")
