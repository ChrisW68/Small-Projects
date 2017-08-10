import glob
import datetime

files=glob.glob("file*.txt")

with open(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")+".txt", 'w') as file:
    for filename in files:
        with open(filename,"r") as f:
            file.write(f.read()+'\n')
