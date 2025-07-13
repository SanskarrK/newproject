def far_to_cel(f):
    return (f - 32) * 5 / 9

f = float(input("Enter temperature in Fahrenheit: "))
print(f"{f} Fahrenheit is {far_to_cel(f)} Celsius")