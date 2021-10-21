import pandas  as pd
import os

os.chdir("/home/anubinda/PycharmProjects/DataPicker/venv/")

dataframe = pd.read_csv('sample1.csv',header=None, skiprows=1,encoding='utf-7')
dataframe.drop(dataframe.index[0], inplace=True)
print(dataframe)
#dataframe.to_csv("sample1.csv",index=False)
