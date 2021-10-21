import pandas
import json

#change the file name which is to be read and also the file name at the end

df = []

df.append(pandas.read_csv('sample1.csv', header=None))
df2 = pandas.read_csv('/home/anviubinda/PycharmProjects/DataPicker/whlist.csv',header = None)
df2.drop([0], axis = 0)
df.append(df2)

final = pandas.concat(df, axis = 1, sort=False)



#print(final)


"""""
#remove the confidence column
for i in range(0,54):
    if (i+1) % 3 == 0:
        print(i)
        df.drop([i], axis=1, inplace = True)
"""""

#adds the column names
#df.columns = ['nose_x','nose_y','neck_x','neck_y','Rshoulder_x','Rshoulder_y','Relbow_x','Relbow_y','Rwrist_x','RWrist_y','LShoulder_x','LShoulder_y','LElbow_xp','LElbow_y','LWrist_x','LWrist_y','RHip_x','RHip_y','RKnee_x','RKnee_y','RAnkle_x','RAnkle_y','LHip_x','LHip_y','LKnee_x','LKnee_y','LAnkle_x','LAnkle_y','REye_x','REye_y','LEye_x','LEye_y','REar_x','REar_y','LEar_x','LEar_y']
#df.columns = ['nose_x','nose_y','neck_x','neck_y','Rshoulder_x','Rshoulder_y','Relbow_x','Relbow_y','Rwrist_x','RWrist_y','LShoulder_x','LShoulder_y',	'LElbow_x','	LElbow_y',	'LWrist_x',	'LWrist_y',	'RHip_x',	'RHip_y',	'RKnee_x',	R'Knee_y',	'RAnkle_x',	'RAnkle_y',	'LHip_x'	,'LHip_y',	'LKnee_x','	LKnee_y',	'LAnkle_x',	'LAnkle_y'	,'REye_x',	'REye_y','	LEye_x',	'LEye_y',	'REar_x'	,'REar_y',	'LEar_x',	'LEar_y']
#print ((df.iloc[:, 0]/229))
#DataFrame.div(other, axis=’columns’, level=None, fill_value=None)


dfw = final.iloc[:,36]
dfh = final.iloc[:,37]
dfnx = final.iloc[:,2] / dfw[:]
dfny = final.iloc[:,3] / dfh[:]

print(dfnx)
print(dfny)
#list = df2.values.tolist()
#for i in range(0,36):
#    print (final.iloc[:,37])

#divide each x,y column by image w and h
for i in range(0,36):
    if i % 2 == 0:
        print("i:",i)
        print("x values")
        final.iloc[:,i] = (final.iloc[:, i]) / (dfw.iloc[:])
        final.iloc[:,i] = (final.iloc[:,i]) - (dfnx.iloc[:])
        print(final.iloc[:,i])
    else:
        print("i:", i)
        print("y values")
        final.iloc[:,i] = (final.iloc[:, i]) / (dfh.iloc[:])
        final.iloc[:,i] = (final.iloc[:, i]) - (dfny.iloc[:])

#add fourth column for action label
#df['class'] = 4
#a = 0

#df['frame'] = ''
#for i in range(len(df)):
#    df['frame'].loc[i] = a
#    a = a + 1

#print(df)

print(final)

final.columns = ['nose_x','nose_y','neck_x','neck_y','Rshoulder_x','Rshoulder_y','Relbow_x','Relbow_y','Rwrist_x','RWrist_y','LShoulder_x','LShoulder_y','LElbow_xp','LElbow_y','LWrist_x','LWrist_y','RHip_x','RHip_y','RKnee_x','RKnee_y','RAnkle_x','RAnkle_y','LHip_x','LHip_y','LKnee_x','LKnee_y','LAnkle_x','LAnkle_y','REye_x','REye_y','LEye_x','LEye_y','REar_x','REar_y','LEar_x','LEar_y', 'width', 'height']
# width and height column values are wrong should drop them manually
#print(final)
final.to_csv (r'check.csv', index= None)
