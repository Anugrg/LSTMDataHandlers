import os
from pathlib import Path
import shutil
import pandas as pd

for dirpath,dirnames,files in os.walk("/home/anubinda/Downloads/new_test_dataset/normal_data/normal"):

    for file in files:
        print(file)
        dataframe = pd.read_csv(dirpath +"/" + file,header=None, skiprows=1, encoding='utf-7')
       
        dataframe.fillna(0,inplace=True)
        #dataframe.drop(dataframe.index[0], inplace=True)
        if len(dataframe.columns)>36:
            for i in range(36,len(dataframe.columns)):
                dataframe.drop([i],axis=1,inplace=True)
        dataframe = dataframe.astype('float64')
        dataframe.columns = ['nose_x','nose_y','neck_x','neck_y','Rshoulder_x','Rshoulder_y','Relbow_x','Relbow_y','Rwrist_x','RWrist_y','LShoulder_x','LShoulder_y',
                              'LElbow_x','LElbow_y','LWrist_x','LWrist_y','RHip_x','RHip_y','RKnee_x','RKnee_y','RAnkle_x','RAnkle_y','LHip_x','LHip_y','LKnee_x',
                              'LKnee_y','LAnkle_x','LAnkle_y','REye_x','REye_y','LEye_x','LEye_y','REar_x','REar_y','LEar_x','LEar_y']
       
        df1 = dataframe.loc[( ( ((dataframe['LShoulder_x'] != 0) | (dataframe['LShoulder_y'] != 0))  | ((dataframe['Rshoulder_x'] != 0) | (dataframe['Rshoulder_y'] != 0)) )
                             & ( ((dataframe['LElbow_x'] != 0) | (dataframe['LElbow_y'] != 0)) | ((dataframe['Relbow_x'] != 0) | (dataframe['Relbow_y'] != 0)) )
                             & ( ((dataframe['LWrist_x'] != 0) | (dataframe['LWrist_y'] != 0)) | ((dataframe['Rwrist_x'] != 0) | (dataframe['RWrist_y'] != 0)) )
                             & ( ((dataframe['LKnee_x'] != 0) | (dataframe['LKnee_y'] != 0)) | ((dataframe['RKnee_x'] != 0) | (dataframe['RKnee_y'] != 0)) )
                             & ( ((dataframe['LHip_x'] != 0) | (dataframe['LHip_y'] != 0)) | ((dataframe['RHip_x'] != 0) | (dataframe['RHip_y'] != 0)) )
                             & ( ((dataframe['LAnkle_x'] != 0) | (dataframe['LAnkle_y'] != 0))  | ((dataframe['RAnkle_x'] != 0) | (dataframe['RAnkle_y'] != 0)) )
                            )]


        """
        # for ch3 and ch4
        df1 = df1.loc[(((df1['Rshoulder_x'] != 0) | (df1['Rshoulder_y'] != 0))
                             & ((df1['Relbow_x'] != 0) | (df1['Relbow_y'] != 0))
                             & ((df1['Rwrist_x'] != 0) | (df1['RWrist_y'] != 0))
                             & ((df1['RKnee_x'] != 0) | (df1['RKnee_y'] != 0))
                             & ((df1['RHip_x'] != 0) | (df1['RHip_y'] != 0))
                             & ((df1['RAnkle_x'] != 0) | (df1['RAnkle_y'] != 0))
                      )]
        """              
        df1.to_csv(dirpath +"/"+ "clean" + file,index=None)                     
        #shutil.move(dirpath +"/"+ "clean" + file ,'/home/anubinda/datasets/')
        #shutil.move(dirpath +"/" + file, '/home/anubinda/original/')
        #new_dir=Path(dirpath / "clean/")
        #new_dir.mkdir()
        #shutil.copy("clean"+file,new_dir)
