import sys

n = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))
nl = sorted(set(l))
d = {nl[i]:i for i in range(len(set(l)))}

for e in l:
    print(d.get(e), end=' ')