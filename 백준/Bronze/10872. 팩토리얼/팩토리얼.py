def fac(n):
    if n == 1:
        return 1
    else:
        return fac(n-1)*n

n = int(input())

if n == 0:
    print(1)
else:
    print(fac(n))