import time
from datetime import datetime as dt



hosts_temp="hosts"
hosts_path=r"C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"
website_list=[""]

while True:
    #if current time is between 8 a.m. to 12:00p.m. and 1:00p.m. to 5:00 p.m. then it will excute
    if dt(dt.now().year, dt.now().month, dt.now().day,16) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,18):
        print("Shame on you!")
        print("You should be working!" + "\n")
        with open(hosts_path,'r+') as file:
            content=file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+ website+"\n")
    else:
        #Open hosts_temp variable in a read and write in the file
        with open(hosts_temp, 'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                #If any website in the website_list appears execute file.write(line)
                if not any(website in line for website in website_list):
                    #Will write down the website in the hosts file
                    file.write(line)
            file.truncate()
        print("Non-work hours, so have fun!")
    #run every 2 seconds
    time.sleep(6)