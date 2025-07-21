# Lambda
add = lambda x, y: x + y

# map
nums = [1, 2, 3]
squared = list(map(lambda x: x**2, nums))

# filter
evens = list(filter(lambda x: x % 2 == 0, nums))

# reduce
from functools import reduce
total = reduce(lambda x, y: x + y, nums)
print(f"Add: {add(5, 10)}, Squared: {squared}, Evens: {evens}, Total: {total}")
