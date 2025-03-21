n = int(input())
m = 1

while True:
    d = len(str(m))
    s = i = m
    for _ in range(d):
        s += i % 10
        i //= 10
    if s == n:
        break
    else:
        m += 1
    if m >= n:
        m = 0
        break
print(m)