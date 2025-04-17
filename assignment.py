age = int(input("Enter your age: "))
if age >= 10 and age <= 20:
    if age == 10:
        print("You are 10")
    elif age > 10 and age <= 15:
        print("You are between 10 and 15")
    else:
        print("You are between 16 and 20")
else:
    print("You are not between 10 and 20")
