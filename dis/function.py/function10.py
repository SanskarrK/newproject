def int_to_cm(inch):
    return int(inch * 2.54)

n = int(input("Enter length in inches: "))

print(f"{n} inches is {int_to_cm(n)} cm")