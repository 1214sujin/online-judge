import sys

n = int(sys.stdin.readline())
x = [0]*n
y = [0]*n

for i in range(n):
    x[i], y[i] = map(int, sys.stdin.readline().split())

print((max(x)-min(x))*(max(y)-min(y)))