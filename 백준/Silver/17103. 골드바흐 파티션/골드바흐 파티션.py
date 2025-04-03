import sys

def 에라토스테네스(n):
    lst = [0, 0] + [i for i in range(2, n+1)]
    ans = []
    
    i = 2
    while i < len(lst):
        for j in range(2*i, n+1, i):
            lst[j] = 0
        ans.append(i)
        i += 1
        while i < len(lst) and lst[i] == 0:
            i += 1
    
    return ans

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    cnt = 0
    소수list = 에라토스테네스(n)
    소수set = set(소수list)

    for i in range(len(소수list)):
        if 소수list[i] > n//2:
            break
        if n-소수list[i] in 소수set:
            cnt += 1
    print(cnt)