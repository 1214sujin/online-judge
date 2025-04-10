import sys

n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))

stack = [lst.pop(0)]
answer = 'Nice'
p = 1

while len(lst) > 0:
    while len(lst) > 0 and stack[-1] == p:
        stack.pop()
        p += 1
        if len(stack) == 0:
            break
    if len(stack) > 0:
        if lst[0] > stack[-1]:
            answer = 'Sad'
            break
    stack.append(lst.pop(0))

if len(lst) > 0:
    answer = 'Sad'

print(answer)