n, k = map(int, input().split())

if k > n//2:
    k = n-k

a = b = 1
for i in range(k):
    a *= n-i
    b *= 1+i

print(a//b)