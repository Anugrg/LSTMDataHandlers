import pandas as pd
import argparse
import os
import os.path
import numpy as np
import re

sit = 0
stand = 0
walk = 0
bend = 0
fall = 0
path = "/home/anubinda/Downloads/ytrain1.csv"
csv = pd.read_csv(path, header=None, encoding='utf-7')
Y_test = csv.values
print(Y_test.shape)
y = np.array(Y_test)


for i in range(len(y)):
  if y[i] == 0:
    sit+=1
  elif y[i] == 1:
    stand+=1
  elif y[i] == 2:
    walk+=1
  elif y[i] == 3:
    bend+=1
  elif y[i] == 4:
    fall+=1

print("sit: ",sit)
print("stand: ",stand)
print("walk: ",walk)
print("bend: ",bend)
print("fall: ",fall)
