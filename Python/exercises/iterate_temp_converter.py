temperatures=[10,-20,-289,100]

def writer(temperatures):
    #Create and write to temperature.txt file all termperature
    #are above -273.15
    with open("temperature.txt",'w') as file:
        for c in temperatures:
            if c > -273.15:
                f=c*9/5+32
                #Convert f from a integer to a string
                file.write(str(f)+"\n")
                print(str(f))

writer(temperatures)



