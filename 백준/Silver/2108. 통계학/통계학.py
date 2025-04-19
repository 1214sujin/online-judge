import sys

n = int(sys.stdin.readline())
a = [int(sys.stdin.readline()) for _ in range(n)]
a.sort()
d = {e: 0 for e in a}
for e in a:
    d[e] += 1

sorted_keys = sorted(d, key=lambda x: d[x], reverse=True)

print(round(sum(a)/n))

print(a[n//2])

if len(sorted_keys) > 2 and d[sorted_keys[0]] == d[sorted_keys[1]]:
    print(sorted_keys[1])
else:
    print(sorted_keys[0])

print(a[-1] - a[0])