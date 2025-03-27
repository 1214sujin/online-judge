import sys

n = int(sys.stdin.readline())
l = list(map(lambda x: (int(x[0]), x[1]), [sys.stdin.readline().split() for _ in range(n)]))

l.sort(key=lambda x: x[0])
for e in l:
    print(e[0], e[1])