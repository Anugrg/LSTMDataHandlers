import os
import pandas as pd
import warnings

max = 0
#warnings.filterwarnings('error')
for dirpath,dirnames,files in os.walk("/home/anubinda/new_skeleton_dataset/datasets_normal/"):
    #print(dirpath)
    for file in files:
        
        dataframe = pd.read_csv(dirpath + file,header=None, skiprows=1,encoding='utf-7')
        #dataframe.fillna(0,inplace=True)
        #dataframe.drop(dataframe.index[0], inplace=True)
        if max == 0:
            max = len(dataframe)
            print(file)
            print(max)
            print("-------------")
        elif max<len(dataframe):
            max = len(dataframe) 
            print(file)
            print(max)
            print("*********")
                

print("longest frameset",max)


