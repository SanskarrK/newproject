def greater():
    
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = int(input("Enter third number: "))

    if a > b and a > c:
        print("the greatest number is:", a)
    elif b > a and b > c:
        print("the greatest number is:", b)
    else:
        print("the greatest number is:", c)

greater()  # function call    