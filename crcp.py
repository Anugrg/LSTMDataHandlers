import pandas as pd
import glob
import os
import shutil
import re
from pathlib import Path

print("starting....")

destination = Path.home() / "dataset" 
print(type(destination))
for subdir, dirs, files in os.walk("/home/anubinda/Downloads/new_test_dataset/normal_data/normal"):
    for file in files:
        if re.search("clean",file):
            dir = subdir
            print(dir)
            new = "clean"
            
            path = os.path.join(dir, new)
            
            if not os.path.exists(path):
                os.mkdir(path)
            print("file => " + path)
            copy_this = subdir + "/" + file
            shutil.move(copy_this, path )
            print("moved => " + copy_this)


print("completed...")
