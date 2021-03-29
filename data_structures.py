print("Python Data Structures Work")
# 1  Arrays / Lists
cars = ["Toyota", "Tesla", "Hyundai"]
print(len(cars))
cars.append("Honda")
cars.pop(1)
for x in cars:
    print(x)

#2 Queue
from collections import deque

q = deque()

q.append('a')
q.append('b')
q.append('c')
print("Initial Q")
print(q)

print(q.popleft())
print(q.popleft())
print(q.popleft())

print("Current Q")
print(q)

