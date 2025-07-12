num = int(input("Enter a number: "))
pro = 1
for i in range(1, num + 1):
    pro *= i
print("The factorial of", num, "is", pro)