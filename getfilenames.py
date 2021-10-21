import glob
import os


path = "/home/anubinda/Videos/aicamvideo/"
os.chdir(path)

iter_filenames = glob.iglob("*.mp4")

f = open("filelist.txt", "a")
for file in iter_filenames:
    f.write(file)
    f.write("\n")


f.close()
