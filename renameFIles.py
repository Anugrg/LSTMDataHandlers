import os
import glob
os.chdir("/home/anubinda/PycharmProjects/DataPicker/venv/used_csv/test/")
count = 1


for dirpath,dirnames,files in os.walk():
    for name in glob.glob('*.csv'):
        os.rename(name,str(count)+".csv")
        count+=1
