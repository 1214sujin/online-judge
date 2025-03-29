import sys

n = int(sys.stdin.readline())
상근 = set(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
카드 = list(map(int, sys.stdin.readline().split()))

for e in 카드:
    if e in 상근:
        print(1, end=' ')
    else:
        print(0, end=' ')