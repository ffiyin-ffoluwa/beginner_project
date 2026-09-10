print("Welcome to Paul's Calculator")
print("What is the passoword")
password = input(" ")
if password.upper() == "FIYIN" :
    print("Welcome")
    q1 = input("Integer or Decimal (I or D): ")
    if q1.upper() == "I":
        f1 = int(input("First Number: "))
        s2 = int(input("Second Number: "))
        sign = input("""
        Type A for Addition
        Type S for Subtraction
        Type D for Divion
        Type M for multiplication
        : """)
        if sign.upper() == "A":
            print (f1 + s2)
        elif sign.upper() == "S":
            print (f1 - s2)
        elif sign.upper() == "D":
            print (f1 / s2)
        elif sign.upper() == "M":
            print (f1 * s2)
        else:
            print("Error")
    elif q1.upper() == "D":
        f1 = float(input("First Number: "))
        s2 = float(input("Second Number: "))
        sign = input("""
        Type A for Addition
        Type S for Subtraction
        Type D for Divion
        Type M for multiplication
        : """)
        if sign.upper() == "A":
            print (f1 + s2)
        elif sign.upper() == "S":
            print (f1 - s2)
        elif sign.upper() == "D":
            print (f1 / s2)
        elif sign.upper() == "M":
            print (f1 * s2)
        else:
            print("Error")
    else:
        print("Error")
else:
    print("Try again: ")
