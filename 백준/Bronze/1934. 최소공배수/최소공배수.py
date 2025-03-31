import sys

def get공약수and몫(a, b):
    i = 2
    while i <= min(a, b):
        if a%i == 0 and b%i == 0:
            return i, a//i, b//i
        i += 1
    return 1, a, b

t = int(sys.stdin.readline())

for _ in range(t):
    공약수list = []
    a, b = map(int, sys.stdin.readline().split())
    while True:
        공약수, a, b = get공약수and몫(a, b)
        if 공약수 == 1:
            break
        공약수list.append(공약수)
    ans = a*b
    for e in 공약수list:
        ans *= e
    print(ans)