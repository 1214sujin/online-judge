import sys

req = sys.stdin.read()
it = iter(map(int, req.split('\n')))

n = 5
l = []
s = 0
for i in range(n):
    nxt = next(it)
    l.append(nxt)
    s += nxt
for i in range(n-1, 0, -1):
    for j in range(i):
        if l[j] > l[j+1]:
            l[j], l[j+1] = l[j+1], l[j]

mean = s//n
mid = l[2]
print(mean)
print(mid)