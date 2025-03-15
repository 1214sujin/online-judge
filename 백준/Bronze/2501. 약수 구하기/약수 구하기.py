n, k = map(int, input().split())

ans = 0
k0 = 0
for i in range(1, n+1):
    if n % i == 0:
       k0 += 1
    if k0 == k:
        ans = i
        break
print(ans)