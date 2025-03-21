a, b, c, d, e, f = map(int, input().split())
check = 0

for x in range(-999, 1000):
    for y in range(-999, 1000):
        if a*x + b*y == c and d*x + e*y == f:
            check = 1
            break
    if check == 1:
        break
print(f'{x} {y}')