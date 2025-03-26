req = input()
ans = [0] * 10

for i in range(len(req)):
    ans[int(req[i])] += 1

for i in range(9, -1, -1):
    for _ in range(ans[i]):
        print(i, end='')