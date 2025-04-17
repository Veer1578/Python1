medicalCause = input("Do you have a medical cause Y or N ")
attendance = int(input("Enter attendance % "))

if medicalCause == "Y":
    print("Allowed")
else:
    if attendance >= 75:
        print("Allowed")
    else:
        print("Not allowed")
