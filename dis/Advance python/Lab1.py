from collections import namedtuple, Counter, defaultdict, deque

Point = namedtuple('Point', 'x y')
p = Point(1, 2)

counter = Counter('banana')
print(counter)  # {'a': 3, 'b': 1, 'n': 2}

d = defaultdict(int)
d['missing'] += 1

q = deque()
q.appendleft(5)
print(f"Point: {p}, Counter: {counter}, Defaultdict: {d}, Deque: {q}")