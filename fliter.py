import numpy as np
import pandas as pd
import argparse


parser = argparse.ArgumentParser(description='extract rows pertaining to subject')
parser.add_argument('--dir', help='path to file')
parser.add_argument('--name', help='Name of file')
parser.add_argument('--save_path', help ='the path to store file')
parser.add_argument('--save_as', help='name of final file')
parser.add_argument('--id',help='track id')
args = parser.parse_args()

# path = "/media/anubinda/5E20-767F/Anubinda/subject_fall/ch1/Fast_walk_F/processed_csv/"
df = pd.read_csv(args.dir + "/" + args.name, header=None, encoding='utf-7')
df.columns = df.iloc[0]
id = args.id
data = df.loc[df['trk_id_no'] == id ]
data.to_csv(r'' + args.save_path + '/' + args.save_as + 'copy.csv', index=False)