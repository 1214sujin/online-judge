def fac(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fac(n-1)*n

print(fac(int(input())))