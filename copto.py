import argparse
import shutil

parser = argparse.ArgumentParser(description='files to copy')
parser.add_argument('--destination', help='path to dest')
parser.add_argument('--start', help='start number')
parser.add_argument('--fin', help='end number')
args = parser.parse_args()

start = int(args.start)
fin = int(args.fin)

for i in range(start, fin):
    try:
        if (i < 10):
            shutil.move('0000' + str(i) + '.jpg', args.destination)
        elif(i >= 10 and i < 100):
            shutil.move('000' + str(i) + '.jpg', arg
            s.destination)
        else:
            shutil.move('00' + str(i) + '.jpg', args.destination)
    except FileNotFoundError:
        continue;

