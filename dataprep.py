import pandas as pd
import glob
import os

os.chdir("/media/anubinda/5E20-767F/EC-TrimmedVideos/processed/ch1/Sagar/Fall/processed_csv/")
files = glob.iglob("*.csv")

for file in files:
    dataFrame = pd.read_csv( file, header = None, encoding='utf-7')
    dataFrame.fillna(0,inplace=True)
    dataFrame.drop(dataFrame.index[0], inplace=True)
    dataFrame.drop(dataFrame.index[0],inplace=True)
    if len(dataFrame.columns) > 36:
        for i in range(36, len(dataFrame.columns)):
            dataFrame.drop([i], axis=1, inplace=True)
    dataFrame = dataFrame.astype('float64')
    # print(dataFrame)
    # print("*****************************************")
    dataFrame.to_csv( "/media/anubinda/5E20-767F/EC-TrimmedVideos/processed/done/Sagar/"+ "fall" + file, index=None, header=None)