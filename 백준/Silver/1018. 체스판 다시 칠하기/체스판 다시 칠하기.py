import sys

input = sys.stdin.read()

it = iter(input.split('\n'))
n, m = map(int, next(it).split())
board = [[]] * n
answer = 1250
chess = [0, 1, 0, 1, 0, 1, 0, 1]

for i in range(n):
    board[i] = [1 if l == 'W' else 0 for l in next(it)]

for i in range(n-7):
    for j in range(m-7):
        s = 0
        for k in range(i, i+8):
            s += sum([board[k][j+l]^chess[l] for l in range(8)])
            chess = [c^1 for c in chess]
        answer = min([answer, s, 64-s])
print(answer)