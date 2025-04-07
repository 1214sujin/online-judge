import sys

t = int(sys.stdin.readline())

for _ in range(t):
    stack = []
    string = sys.stdin.readline()
    vps = 'YES'
    
    for c in string:
        if c == '(':
            stack.append(1)
        else:
            if c == ')':
                if len(stack) > 0:
                    stack.pop()
                else:
                    vps = 'NO'
                    break
    if len(stack) > 0:
        vps = 'NO'
    print(vps)