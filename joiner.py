import pandas as pd
import sys
import fnmatch
import glob
import csv


dfs = []
print (type(dfs))
for file in glob.glob("*.csv"):
    print(file)
    dfs.append(pd.read_csv(file))
    #print (dfs)

finaldf = pd.concat(dfs, sort=False)
print (finaldf.shape)
finaldf.to_csv("final_pose_ch1_5_classes.csv")


#print (dfs[2].axes)
