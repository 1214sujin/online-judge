import sys

n, m = map(int, sys.stdin.readline().split())
s = set([sys.stdin.readline() for _ in range(n)])
mlist = [sys.stdin.readline() for _ in range(m)]
ans = 0

for e in mlist:
    if e in s:
        ans += 1
print(ans)