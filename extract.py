import pandas as pd
import argparse


parser = argparse.ArgumentParser(description='create seperate csv files for different action one csv output of one video')
parser.add_argument('--directory', help='Path to directory of csv file.')
parser.add_argument('--name', help='Name of file')
parser.add_argument('--action',help='Name of action')
parser.add_argument('--start_frame', help ='the frames where action occurs')
parser.add_argument('--end_frame', help = 'the frames where action stops')
parser.add_argument('--path', help ='the path to folder to save csv file')
args = parser.parse_args()

data = pd.read_csv(args.directory + "/" + args.name, header=None, encoding='utf-7')

start = int(args.start_frame) - 1
end = int(args.end_frame)
print("starting frame", start)
print("ending frame", end)
print(data.columns)
data.drop(columns=[36], inplace=True)
copy = data.iloc[start:end, :].copy()

copy.to_csv(r'' + args.path + "/" + args.name +'.csv', index=False, header=False)
