import os
import pandas as pd
import shutil
from pathlib import Path

destination = Path.home() / "discard" 
for dirpath,dirnames,files in os.walk("/home/anubinda/Documents/Eldercare/Psong_house_test_dataset/normal_data/stand-halfbody/half-body/superclean/"):
    
    for file in files:
        print(file)
        
        dataframe = pd.read_csv(dirpath + "/" + file,header=None, skiprows =1 ,encoding='utf-7')
        
        #dataframe.fillna(0,inplace=True)
        #dataframe.drop(dataframe.index[0], inplace=True)
        if len(dataframe) < 5:
            print(len(dataframe))
            #shutil.move(dirpath+"/"+file,  destination)
            print(file)
        if dataframe.empty:
            print(file)    





