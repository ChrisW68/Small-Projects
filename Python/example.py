import datetime

r"""
This script creates an empty file
"""

filename=datetime.datetime.now()

#Create empty file
def create_file():
    with open(filename.strftime("%Y-%m-%d-%H-%M")+".txt","w") as file:
        file.write("") #writing to file
create_file()

file.r