import sys

n = int(sys.stdin.readline())
l = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]

l.sort(key=lambda x: (x[1], x[0]))
for i in range(n):
    print(l[i][0], l[i][1])