import sys
import collections

n = int(sys.stdin.readline())
deq = collections.deque()

for _ in range(n):
    c = list(map(int, sys.stdin.readline().split()))
    if c[0] == 1:
        deq.appendleft(c[1])
    elif c[0] == 2:
        deq.append(c[1])
    elif c[0] == 5:
        print(len(deq))
    elif c[0] == 6:
        if len(deq) == 0:
            print(1)
        else:
            print(0)
    
    elif len(deq) == 0:
        print(-1)
      
    elif c[0] == 3:
        print(deq.popleft())
    elif c[0] == 4:
        print(deq.pop())
    elif c[0] == 7:
        print(deq[0])
    elif c[0] == 8:
        print(deq[-1])