import sys

req = sys.stdin.read()
it = iter(map(int, req.split('\n')))

n = next(it)
ns = []
for i in range(n):
    ns.append(next(it))

for i in range(n-1, 0, -1):
    for j in range(i):
        if ns[j] > ns[j+1]:
            ns[j], ns[j+1] = ns[j+1], ns[j]

for i in range(n):
    print(ns[i])