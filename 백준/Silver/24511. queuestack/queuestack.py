import sys
import collections

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
c = list(map(int, sys.stdin.readline().split()))

q = collections.deque([b[i] for i in range(n) if a[i]==0])

for i in range(m):
    q.appendleft(c[i])
    print(q.pop(), end=' ')