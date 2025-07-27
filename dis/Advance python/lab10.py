def division(n):
    if(n%10 ==0):
        return True
    return False

a = [1,3,5,10000,23,57,34,67,10]

f = list(filter(division,a))
print(f)