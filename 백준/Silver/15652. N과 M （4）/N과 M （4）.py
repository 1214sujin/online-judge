import sys

n, m = map(int, sys.stdin.readline().split())
answer = []

def print_sy(answer):
    for a in answer:
        print(a+1, end=' ')
    print()

def dfs():
    if len(answer) == m:
        print_sy(answer)
    else:
        for i in range(n):
            if len(answer) == 0 or i >= answer[-1]:
                answer.append(i)
                dfs()
                answer.pop()

dfs()