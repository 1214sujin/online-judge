import sys
import collections

n = int(sys.stdin.readline())
cmd = sys.stdin.readline().split()
deq = collections.deque([(str(x+1), int(cmd[x])) for x in range(n)])
answer = []

def nxt(d):
    if d >= 0:
        for _ in range(d-1):
            deq.append(deq.popleft())
        p, d = deq.popleft()
    else:
        for _ in range(-d-1):
            deq.appendleft(deq.pop())
        p, d = deq.pop()
    answer.append(p)
    return d

dist = nxt(0)

while len(deq) > 0:
    dist = nxt(dist)

for i in range(n):
    print(answer[i], end=' ')