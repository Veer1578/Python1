print("Select your operation ")
print("1.Add")
print("2.Subtract")
print("3.Divide")
print("4.Multiply")

choice = int(input("Enter choice "))

num1 = float(input("Enter number "))
num2 = float(input("Enter another number "))

if choice == 1:
    print("Result = ", num1 + num2)
elif choice == 2:
    print("Result = ", num1 - num2)
elif choice == 3:
    if num2 != 0:
        print("Result = ", num1 / num2)
    else:
        print("Division by 0 not allowed")
elif choice == 4:
    print("Result = ", num1 * num2)
else:
    print("Invalid Choice")
