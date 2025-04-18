import sys

n = int(sys.stdin.readline())
s = {'ChongChong'}

for _ in range(n):
    a, b = sys.stdin.readline().split()
    if a in s:
        s.add(b)
    elif b in s:
        s.add(a)

print(len(s))