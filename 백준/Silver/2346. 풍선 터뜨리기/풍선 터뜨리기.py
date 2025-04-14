import sys
import collections

n = int(sys.stdin.readline())
cmd = list(map(int, sys.stdin.readline().split()))
deq = collections.deque([(x+1, cmd[x]) for x in range(n)])
answer = []

def pop(d):
    if d >= 0:
        p, d = deq.popleft()
    else:
        p, d = deq.pop()
    answer.append(p)
    return d
def nxt(d):
    if d > 0:
        for _ in range(d-1):
            deq.append(deq.popleft())
        return pop(d)
    
    else:
        for _ in range(-d-1):
            deq.appendleft(deq.pop())
        p = pop(d)
        return p

dist = pop(0)

while len(deq) > 0:
    dist = nxt(dist)

for i in range(n):
    print(answer[i], end=' ')