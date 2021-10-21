import pandas as pd
import glob
import os

os.chdir("/media/anubinda/5E20-767F/Anubinda/temp/Test/Normal(subject7)/sit_stand/ch2/standing/")
#os.mkdir("/media/anubinda/5E20-767F/Anubinda/temp/Test/Normal(subject7)/sit_stand/ch2/standing/clean/")
iter_filenames = glob.iglob("*.csv")
for file in iter_filenames:
    dataframe = pd.read_csv(file,header=None, encoding='utf-7')
    dataframe.drop(dataframe.index[0], inplace = True)

    if len(dataframe.columns)>36:
        for i in range(36,len(dataframe.columns)):
            dataframe.drop([i],axis=1,inplace=True)

    dataframe.fillna(0, inplace=True)
    dataframe = dataframe.astype('float64')
    #print(dataframe[0] < '0.25')
    # dataframe.columns = ['nose_x','nose_y','neck_x','neck_y','Rshoulder_x','Rshoulder_y','Relbow_x','Relbow_y','Rwrist_x','RWrist_y','LShoulder_x','LShoulder_y','LElbow_x','LElbow_y','LWrist_x','LWrist_y','RHip_x','RHip_y','RKnee_x','RKnee_y','RAnkle_x','RAnkle_y','LHip_x','LHip_y','LKnee_x','LKnee_y','LAnkle_x','LAnkle_y','REye_x','REye_y','LEye_x','LEye_y','REar_x','REar_y','LEar_x','LEar_y']

    print(dataframe.select_dtypes(include=['float64']))
    print(dataframe.values)

    # df1.to_csv("/media/anubinda/5E20-767F/Anubinda/temp/Test/Normal(subject7)/sit_stand/ch2/standing/clean/" + "clean" + file,
    #            index=None)





