def multiply(n):
    for i in range(1, n + 1):
        print(f"{n} x {i} = {n * i}")

n = int(input("Enter a number to multiply: "))
multiply(n)