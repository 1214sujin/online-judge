m, n = tuple(map(int, input().split()))
req = [i for i in range(2, n+1)]

i = 0
while (i+2)*2 <= n:
    for j in range(req[i]*2-2, len(req), req[i]):
        req[j] = 0
    i += 1
    while req[i] == 0:
        i += 1

for i in req:
    if i != 0 and i >= m:
        print(i)