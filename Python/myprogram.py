def age_old(age):
    new_age = age + 5
    return new_age

def age_young(age):
    new_age = age + 5
    return new_age

age2 = float(input("Enter your age: "))

if age2 < 30:
    print(age_young(age2))
else:
    print("You are an old: ", age_old(age2))
