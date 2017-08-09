import glob

filename = glob.glob('./file*.txt')

with open("file1.txt","r") as file:
    content=file.read()
    print(content)
with open("filetest.txt","a+") as filetransfer:
    filetransfer.write(content)
    print(content)
file.close()

