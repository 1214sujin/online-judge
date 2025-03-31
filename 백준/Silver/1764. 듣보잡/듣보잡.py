n, m = map(int, input().split())
듣 = set([input() for _ in range(n)])
보 = [input() for _ in range(m)]

cnt = 0
듣보 = []

for e in 보:
    if e in 듣:
        cnt += 1
        듣보.append(e)
듣보.sort()

print(cnt)
for e in 듣보:
    print(e)