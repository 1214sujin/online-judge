import sys

req = sys.stdin.read()
it = iter(req.split('\n'))

n = int(next(it))
l = [int(next(it)) for i in range(n)]

l.sort()
for i in range(n):
    print(l[i])