import subprocess
import glob
import os

#os.chdir("/home/anubinda//eldercare/software/apps/EldercareTest/")
#files = glob.iglob("*.cpp")
#for name in files:
#    print("The list:")
#    print(name)

#print("break")

for dirnames,dirpath,files in os.walk("/home/anubinda/Pictures"):
    #for files in glob.glob('*.cpp'):
    for file in files:
        print(file)
        #os.system( "sh justecho.sh " + file)
        subprocess.call(['sh', './justecho.sh' , file] )
        print("done")

print("fin")
