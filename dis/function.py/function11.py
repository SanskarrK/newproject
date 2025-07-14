name = ["Sanskar", "sanskriti", "sanjana", "sanjay", "santosh", "santosh", "santosh", "santosh"]

def rem(name, n):
    if n in name:
        name.remove(n)
    return name

n = input("Enter name to remove: ")

print(rem(name, n))