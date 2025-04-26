n, m = map(int, input().split())
visited = [False] * n
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
            if visited[i] == False:
                answer.append(i)
                visited[i] = True
                dfs()
                visited[i] = False
                answer.pop()

dfs()