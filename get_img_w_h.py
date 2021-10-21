import pandas as pd
import sys
import glob
import csv
from PIL import Image

width = []
height = []
for file in glob.glob("/home/anubinda/PycharmProjects/DataPicker/venv/*.png"):
    im = Image.open(file)
    width.append(im.width)
    height.append(im.height)

print(width)
print(height)

wh =  list(zip(width,height))
print (wh)

# Create a dataframe from zipped list
df = pd.DataFrame(wh, columns=['width', 'height'])
print(df)

df.to_csv("whlist.csv")



