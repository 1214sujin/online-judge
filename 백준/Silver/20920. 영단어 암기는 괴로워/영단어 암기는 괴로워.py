import sys

n, m = map(int, sys.stdin.readline().split())
lst = [sys.stdin.readline().split()[0] for _ in range(n)]
a = [e for e in lst if len(e)>=m]
d = {e: 0 for e in a}
for e in a:
    d[e] += 1
a = list(set(a))

a.sort()
a.sort(key=lambda x: len(x), reverse=True)
a.sort(key=lambda x: d[x], reverse=True)

for a in a:
    print(a)