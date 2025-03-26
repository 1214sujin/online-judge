import sys

n = int(sys.stdin.readline())
a = [0] * 10000

for i in range(n):
    a[int(sys.stdin.readline())-1] += 1

for i in range(10000):
    for _ in range(a[i]):
        print(i+1)