import sys

a, b, c = map(int, sys.stdin.readline().split())
a, b, c = sorted([a, b, c])

if c >= a+b:
    print((a+b)*2-1)
else:
    print(a+b+c)