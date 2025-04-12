import sys
import collections

n = int(sys.stdin.readline())
q = collections.deque([x+1 for x in range(n)])

while len(q) > 1:
    q.popleft()
    if len(q) == 1:
        break
    q.append(q.popleft())
print(q[0])