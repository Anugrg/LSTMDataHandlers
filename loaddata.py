import pandas as pd
import argparse
import os
import os.path
import numpy as np
import re

def process_csv(csv, label):
  temp = csv.values
  data = temp.astype(float)
  x = []
  y = []
  if len(data) < 40:
    print("less than 40 frames")
    pad = create_pad()
    # print("pad",pad)
    data = pad_sequence(data, pad)
    # print("data",data)
    x.append(data)
    # print(np.array(x).shape)
  elif len(data) >= 40:
    # print("greater than 40 frames")
    for i in range(40, len(data)):
      x.append(data[i - 40:i])
  print(np.array(x).shape)
  n = len(x)  # length will be 1 for shorter frames as only 1 sequence of 40 can be made after padding
  print("n", n)
  y = create_labels(n, label)
  return x, y


def create_labels(n, lab):
  Y = []
  if lab == 0:
    for j in range(n):
      Y.append([0])
  elif lab == 1:
    for j in range(n):
      Y.append([1])
  elif lab == 2:
    for j in range(n):
      Y.append([2])
  elif lab == 3:
    for j in range(n):
      Y.append([3])
  elif lab == 4:
    for j in range(n):
      Y.append([4])
  return Y


def pad_sequence(data, pad):
  print("inside pad sequence")
  # print(data)
  # print("pad",pad)
  if len(data) < 40:
    gap = 40 - len(data)
    # print("spread: ",gap)
    for i in range(gap):
      data = np.vstack((data, pad))
  return data


def create_pad():
  pad = []
  for i in range(0, 36):
    pad.append(0.0)
  return pad


def one_hot_encoder(data):
  one_hot_y = tf.one_hot(data.astype(np.int32), depth=5, axis=1, dtype=tf.int32)
  return one_hot_y

X_test = []
Y_test = []
label = 0
directory = "/media/anubinda/5E20-767F/Anubinda/new_dataset_3/Test/"

for dir_path, dir_names, files in os.walk(directory):
  for file in files:
    if re.search("sit", file):
      label = 0
    elif re.search("stand", file):
      label = 1
    elif re.search("walk", file):
      label = 2
    elif re.search("bend", file):
      label = 3
    elif re.search("fall", file):
      label = 4

    path = dir_path + "/" + file
    print(path)
    csv = pd.read_csv(path, header=None, encoding='utf-7')
    csv.drop(csv.index[0], inplace=True)
    if len(csv.columns) > 36:
      for i in range(36,len(csv.columns)):
        csv.drop([i], axis=1, inplace=True)
    temp_x, temp_y = process_csv(csv, label)
    X_test.extend(temp_x)
    Y_test.extend(temp_y) 

sit = 0
stand = 0
walk = 0
bend = 0
fall = 0
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

