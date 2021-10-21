import os
from collections import OrderedDict
from glob import iglob
import csv

os.chdir("/home/anubinda/PycharmProjects/DataPicker/venv/")
files = sorted(iglob('*.csv'))
header = OrderedDict()
data = []
for filename in files:
    with open(filename, 'r') as fin:
        csvin = csv.DictReader(fin)
        header.update(OrderedDict.fromkeys(csvin.fieldnames))
        data.append(next(csvin))
        print(data)
with open('combined_pose.csv', 'w', newline='') as fout:
    csvout = csv.DictWriter(fout, fieldnames=list(header))
    csvout.writeheader()
    csvout.writerows(data)










"""""
extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
print(all_filenames)


#combine all files in the list
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
#export to csv
combined_csv.to_csv( "train_examples.csv", index=False, encoding='utf-8-sig')
"""""