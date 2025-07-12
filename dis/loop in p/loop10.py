num = int(input("Enter a number: "))

for i in range(1, num):
    print(" "* (num - i), end="")
    print("*" * (2 * i - 1), end="")
    print("")