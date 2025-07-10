num =int(input("Enter a number: "))
i=1
while(i <= num):
    factorial = 1
    while(i <= num):
        factorial = factorial * i
        i = i + 1
    print(f"The factorial of {i} is {factorial}")