import sys

def 호제법(a, b):
    b, a = sorted([a, b])
    r = a%b
    if r==0:
        return b
    else:
        return 호제법(b, r)

def get공약수and몫(a, b):
    i = 2
    r = 호제법(a, b)
    return r, a//r, b//r

a1, b1 = map(int, sys.stdin.readline().split())
a2, b2 = map(int, sys.stdin.readline().split())

a = a1*b2 + a2*b1
b = b1*b2

while True:
    공약수, a, b = get공약수and몫(a, b)
    if 공약수 == 1:
        break

print(a, b)