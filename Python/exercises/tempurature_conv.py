def cel_fah(temp):
    fahrenheit = (float(temp) * (9/5))+32
    return fahrenheit
temp2 = input("Enter celsius to convert: ")


print(cel_fah(temp2))