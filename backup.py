import pandas as pd
import argparse
import os
import os.path
import numpy as np
import re
import tensorflow as tf
from sklearn.utils import class_weight

""" This program assumes that the csv files have 
been divided according to the camera channels or angles and the action
classes 
"""

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
    n = len(x) # length will be 1 for shorter frames(len(x)<40) as only 1 sequence of 40 can be made after padding
    print("n",n)
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
    for i in range(0, 36):#24
        pad.append(0.0)
    return pad


def one_hot_encoder(data):
    one_hot_y = tf.one_hot(data.astype(np.int32), depth=5, axis=1, dtype=tf.int32)
    return one_hot_y

def load_data(directory): 
  X = []
  Y = []
  for dir_path, dir_names, files in os.walk(directory):
    for file in files:
      if re.search("sit", file): #time #sit
        label = 0
      elif re.search("stand", file): #clap #stand
        label = 1
      elif re.search("walk", file): #call  #walk
        label = 2
      elif re.search("bend", file): #point #bend
        label = 3
        print("yes")
      elif re.search("fall", file): #wave #fall
        label = 4
   
      path = dir_path + "/" + file
      print(path)
      print("label",label)
      csv = pd.read_csv(path, header=None, encoding='utf-7')
      csv.drop(csv.index[0], inplace=True)
      if csv.empty:
        print("empty: "+ path)    
        break
      if len(csv.columns) > 36: #24
        for i in range(36,len(csv.columns)): #24
          csv.drop([i], axis=1, inplace=True)
      is_NaN = csv.isnull()
      if any(is_NaN.any(axis=1)) == True:
        print(path)
      csv.fillna(0.0,inplace=True)  
      temp_x, temp_y = process_csv(csv, label)
      X.extend(temp_x)
      Y.extend(temp_y)
  return X,Y

# ch1, ch2, ch3, ch4
# fall, sit, walk, bend, stand

file_names = ["Train/" ,"Test/"] #, "validation/"] 
directory = ["/content/drive/My Drive/lstm models/" + i for i in file_names] 
#directory = ["/content/drive/My Drive/lstm models/csv-lstm/train/"]
label = 0
X_train, Y_train = load_data(directory[0])
X_test, Y_test = load_data(directory[1])
#X_val, Y_val = load_data(directory[2])

# convert into numpy arrays from list 
X_train = np.array(X_train)
X_test = np.array(X_test)
#X_val = np.array(X_val)
Y_train = np.array(Y_train)
Y_test = np.array(Y_test)
#Y_val = np.array(Y_val)
Y_train_1 = Y_train 
Y_test_1 = Y_test
#Y_val_1 = Y_val

print(Y_train[0])
print( np.unique(Y_train))
# for imbalanced class otherwise comment out
class_weight = class_weight.compute_class_weight('balanced', np.unique(Y_train), Y_train.reshape(-1))
class_weight = {0: class_weight[0], 1: class_weight[1], 2: class_weight[2], 3: class_weight[3], 4: class_weight[4]    }

# To get vector like [0 0 0 1 0] results in Y
Y_train = np.array(one_hot_encoder(Y_train)).reshape(-1, 5).astype(np.int32)
Y_test = np.array(one_hot_encoder(Y_test)).reshape(-1, 5).astype(np.int32)
#Y_val = np.array(one_hot_encoder(Y_val)).reshape(-1, 5).astype(np.int32)




