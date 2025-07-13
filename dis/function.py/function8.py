def sum(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * sum(n-1) 

n = int(input("Enter a number: "))
print(f"The sum of numbers from 1 to {n} is {sum(n)}")