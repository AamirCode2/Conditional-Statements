medical_cause = str(input("Did you have a medical cause, yes or no: "))
atten = int(input("Enter your attendance level: "))

if medical_cause == "yes":
    print("You are allowed to write the exam")
else:
    if atten >= 75:
        print("You are allowed to write the exam")
    else:
        print("You are not allowed to write the exam")