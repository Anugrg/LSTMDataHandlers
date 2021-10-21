import pandas as pd
import glob
import os
import shutil
import re
from pathlib import Path

print("starting....")

destination = Path.home() / "dataset" 
print(destination)
for subdir, dirs, files in os.walk("/home/anubinda/Downloads/new_test_dataset/normal_data/normal"):
    for file in files:
        if re.search("clean",file):
            dir = subdir
            print(subdir)
            print("destination ",destination)
            path = os.path.join(destination,dirs)
            print("path =",path)
            if not os.path.exists(path):
                os.mkdir(path)
            print("file => " + path)
            copy_this = subdir + "/" + file
            print(copy_this)
            shutil.move(copy_this, path )
            print("moved => " + copy_this)


print("completed...")
