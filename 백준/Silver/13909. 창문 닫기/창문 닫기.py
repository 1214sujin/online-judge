import sys

n = int(sys.stdin.readline())
ans = 0

i = 1
while i**2 <= n:
    ans += 1
    i += 1

print(ans)