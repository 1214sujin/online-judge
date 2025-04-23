import sys

def cantor(n):
    if n == 0:
        return '-'
    return cantor(n-1) + ' '*3**(n-1) + cantor(n-1)

for line in sys.stdin.readlines():
    n = int(line)
    print(cantor(n))