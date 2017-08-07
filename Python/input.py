def currency_converter(rate,euros):
    dollars=euros*rate
    return dollars
r=input("Enter the rate: ")
e=input("Enter the euros: ")
print(currency_converter(float(r),float(e)))