import glob

for filename in glob.glob('./file?.txt'):

    with open(filename) as file:
        content=file.read()
    with open("filetest.txt",'a') as filetransfer:
        filetransfer.write(content+'\n')
    file.close()
    filetransfer.close()

