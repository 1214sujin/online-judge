import sys

input = sys.stdin.read()

it = iter(input.split('\n'))
n, m = map(int, next(it).split())
board = [[]] * n
answer = 1250
chess = 'WBWBWBWB'

for i in range(n):
    board[i] = next(it)

for i in range(n-7):
    for j in range(m-7):
        s = 0
        for k in range(i, i+8):
            s += sum([0 if board[k][j+l] == chess[l] else 1 for l in range(8)])
            chess = ['W' if c == 'B' else 'B' for c in chess]
        answer = min([answer, s, 64-s])
print(answer)