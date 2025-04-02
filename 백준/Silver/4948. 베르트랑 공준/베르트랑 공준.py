import sys

def 에라토스테네스(n):
    lst = [i for i in range(2*n+1)]
    
    lst[1] = 0
    i = 2
    
    while i < len(lst):
        for j in range(2*i, 2*n+1, i):
            lst[j] = 0
        i += 1
        while i < len(lst) and lst[i] == 0:
            i += 1
    
    i = 2
    while lst[i] <= n:
        i += 1
    ans = []
    for j in range(i, 2*n+1):
        if (lst[j] != 0):
            ans.append(j)
    return ans

n = int(sys.stdin.readline())
while n > 0:
    print(len(에라토스테네스(n)))
    n = int(sys.stdin.readline())