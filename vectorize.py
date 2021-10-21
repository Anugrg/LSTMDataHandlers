import pandas
import numpy as np
from math import sqrt

df = pandas.read_csv('/home/anubinda/Downloads/xtrestv.csv - Sheet2 - xtrestv.csv - Sheet1.csv',header = None)

data = df.values.tolist()

print(len(data[0]))

key_vectors = list()

l = len(data)





def from_neck( data  ):

     temp = list()
     if sum_root(data[4], data[5], data[2], data[3]) == 0.0:
         temp.append(0.0)
         temp.append(0.0)
     else:
         temp.append((data[4] - data[2])/ sum_root( data[4], data[5], data[2], data[3]) )
         temp.append((data[5] - data[3]) / sum_root(   data[4], data[5], data[2], data[3]))
     if sum_root( data[10],data[11], data[2],data[3]) == 0.0:
         temp.append(0.0)
         temp.append(0.0)
     else:
         temp.append((data[10] - data[2]) / sum_root(data[10], data[11], data[2], data[3]))
         temp.append((data[11] - data[3]) / sum_root(data[10], data[11], data[2], data[3]))
     if sum_root( data[12],data[13], data[10], data[11]) == 0.0:
         temp.append(0.0)
         temp.append(0.0)
     else:
         temp.append(( data[12] - data[10] ) / sum_root( data[12],data[13], data[10], data[11]))
         temp.append(( data[13] - data[11] ) / sum_root( data[12],data[13], data[10], data[11]))

     if sum_root( data[6],data[7], data[4], data[5]) == 0.0:
         temp.append(0.0)
         temp.append(0.0)
     else:
         temp.append(( data[6] - data[4] ) / sum_root( data[6],data[7], data[4], data[5]))
         temp.append((data[7] - data[5]) / sum_root(data[6], data[7], data[4], data[5]))

     if sum_root( data[14],data[15], data[12], data[13]) == 0.0:
         temp.append(0.0)
         temp.append(0.0)
     else:
         temp.append(( data[14] - data[12] ) / sum_root( data[14],data[15], data[12], data[13]))
         temp.append((data[15] - data[13]) / sum_root(data[14], data[15], data[12], data[13]))

     if sum_root(data[8], data[9], data[6], data[7]) == 0.0:
         temp.append(0.0)
         temp.append(0.0)
     else:
         temp.append((data[8] - data[6]) / sum_root(data[8], data[9], data[6], data[7]))
         temp.append((data[9] - data[7]) / sum_root(data[8], data[9], data[6], data[7]))

     if sum_root(data[22], data[23], data[2], data[3])== 0.0:
         temp.append(0.0)
         temp.append(0.0)
     else:
         temp.append((data[22] - data[2]) / sum_root(data[22], data[23], data[2], data[3]))
         temp.append((data[23] - data[3]) / sum_root(data[22], data[23], data[2], data[3]))

     if sum_root(data[16], data[17], data[2], data[3]) == 0.0:
         temp.append(0.0)
         temp.append(0.0)
     else:
         temp.append((data[16] - data[2]) / sum_root(data[16], data[17], data[2], data[3]))
         temp.append((data[17] - data[3]) / sum_root(data[16], data[17], data[2], data[3]))

     if sum_root(data[24], data[25], data[22], data[23]) == 0.0:
         temp.append(0.0)
         temp.append(0.0)
     else:
         temp.append((data[24] - data[22]) / sum_root(data[24], data[25], data[22], data[23]))
         temp.append((data[25] - data[23]) / sum_root(data[24], data[25], data[22], data[23]))

     if sum_root(data[18], data[19], data[16], data[17]) == 0.0:
         temp.append(0.0)
         temp.append(0.0)
     else:
         temp.append((data[18] - data[16]) / sum_root(data[18], data[19], data[16], data[17]))
         temp.append((data[19] - data[17]) / sum_root(data[18], data[19], data[16], data[17]))

     if sum_root(data[26], data[27], data[24], data[25]) == 0.0:
         temp.append(0.0)
         temp.append(0.0)
     else:
         temp.append((data[26] - data[24]) / sum_root(data[26], data[27], data[24], data[25]))
         temp.append((data[27] - data[25]) / sum_root(data[26], data[27], data[24], data[25]))

     if sum_root(data[20], data[21], data[18], data[19]) == 0.0:
         temp.append(0.0)
         temp.append(0.0)
     else:
         temp.append((data[20] - data[18]) / sum_root(data[20], data[21], data[18], data[19]))
         temp.append((data[21] - data[19]) / sum_root(data[20], data[21], data[18], data[19]))
     return(temp)








#sqrt((data[4] - data[2]) ^ 2 + (data[5] - data[3]) ^ 2))

def sum_root(rx,ry ,lx,ly ):
    a = (rx-lx) * (rx-lx)
    b = (ry-ly) * (ry-ly)
    ret = sqrt(a+b)
    if ret == 0.0:
        print("zero division")

    return sqrt(a+b)

for i in range(l):
    key_vectors.append(from_neck(data[i]))


print(key_vectors[0])

final = pandas.DataFrame(key_vectors)
final.to_csv (r'Xtest_vectorized.csv', index= None)