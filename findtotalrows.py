import os
import shutil
import pandas as pd

sum = 0
for dirpath,dirnames,files in os.walk("/home/anubinda/new_skeleton_dataset/datasets_normal/"):
    
    for file in files:
        #print(file)
        try:
            dataframe = pd.read_csv(dirpath + file,skiprows = 1,header=None,encoding='utf-7')
            dataframe.fillna(0,inplace=True)
            #print(len(dataframe))
            #dataframe.drop(dataframe.index[0], inplace=True)
            sum = sum + len(dataframe)
            #print("********************")
        except pd.errors.EmptyDataError:
            shutil.move(dirpath + file,'/home/anubinda/empty_csv/normal_discarded/')
            pass
             
        

print("number of rows",sum)


