def cel_fah(temp):
    fahrenheit = (temp) * (9/5)+ 32
    return fahrenheit
temp2 = float(input("Enter celsius to convert: "))
low_temp = float(-273.15)

if temp2 > low_temp:
    print(cel_fah(temp2))
else:
    print("Too low and cannot exist")