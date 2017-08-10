import glob
#Retreives all files in a directory that is file_.txt
for filename in glob.glob('./file?.txt'):

    #Open the variable 'filename'
    with open(filename) as file:
        #Reads the content of the file from filename variable
        content=file.read()
    #Append to filetest.txt all content from the content variable
    with open("filetest.txt",'a') as filetransfer:
        #writes content into the filetest.txt
        filetransfer.write(content+'\n')
    #closes
    file.close()
    filetransfer.close()

