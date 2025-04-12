import sys

n, k = map(int, sys.stdin.readline().split())
lst = [x+1 for x in range(n)]
answer = []

i = k = k-1

while len(lst) > 1:
    answer.append(lst.pop(i))
    i = (i+k)%len(lst)
answer.append(lst.pop(i))

print('<', end='')
for i in range(n-1):
    print(answer[i], end=', ')
print(answer[n-1], end='>')