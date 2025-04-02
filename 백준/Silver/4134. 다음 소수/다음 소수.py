import sys

def solution(n):
    i = 2
    while i <= n**0.5:
        if n%i == 0:
            return False
        i += 1
    return True

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    if n < 2:
        print(2)
        continue
    while True:
        if solution(n):
            break
        n += 1
    print(n)