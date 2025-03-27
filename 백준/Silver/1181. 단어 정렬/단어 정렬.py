import sys

n = int(input())
l = list(set([input() for _ in range(n)]))

l.sort(key=lambda x: (len(x), x))
for e in l:
    print(e)