import sys

n = int(sys.stdin.readline())
l = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]

l.sort()
for i in range(n):
    print(f'{l[i][0]} {l[i][1]}')