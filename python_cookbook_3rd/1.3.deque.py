#!/usr/bin/env python3

from collections import deque

q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
print(q)

q.append(4)
print(q)

q.append(5)
print(q)

q = deque()
q.append(1)
q.append(2)
q.append(3)
print(q)
print(q.pop())
print(q.popleft())
q.appendleft(4)
print(q)