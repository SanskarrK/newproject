num =int(input("Enter a number: "))

for i in range(1, num):
    if(num % i == 0):
        print("not prime number")
    else:
        print("prime number")
        break