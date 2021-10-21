import numpy as no
import pandas as pd
import os



def process_csv(csv,label):
    temp = csv.values
    data = temp.astype(float)
    x = []
    y = []
    if label == 4:
        if len(data) < 40:
            pad = create_pad()
            data = pad_sequence(data,pad)
            x.append(data)
        elif len(data) >= 40:
            x.append(data[:41])
    else:
        frame = []
        num_framesets = int((len(data) - 40)/(40*(1-0.8125)))+1     
        for frameset in range(0,num_framesets):
            start = int(frameset*40*(1-0.8125))
            for i in range(  start, (start+40)  ):
                frame.append(np.array(data[start]))
        x.extend(frame)          
        
                   
    n = len(x)
    y = create_labels(n,label)
    return x,y 

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
      elif re.search("Fall", file): #wave #fall
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
