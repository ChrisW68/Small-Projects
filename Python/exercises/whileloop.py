password=''
auth_pass='python123'
while password !=auth_pass:
    password=input('Enter password: ')
    if password == auth_pass:
        print("You are logged in")
    else:
        print("Sorry, try again")