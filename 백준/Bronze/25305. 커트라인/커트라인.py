import sys

req = sys.stdin.read()
it = iter(req.split('\n'))

n, k = map(int, next(it).split())
scores = list(map(int, next(it).split()))

scores.sort()
print(scores[-k])