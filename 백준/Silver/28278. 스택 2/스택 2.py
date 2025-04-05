import sys

n = int(sys.stdin.readline())
l = []

for i in range(n):
    c = sys.stdin.readline()
    if c[0] == '1':
        l.append(int(c.split()[1]))
    elif c[0] == '2':
        if len(l) > 0:
            print(l.pop())
        else:
            print(-1)
    elif c[0] == '3':
        print(len(l))
    elif c[0] == '4':
        if len(l) == 0:
            print(1)
        else:
            print(0)
    elif c[0] == '5':
        if len(l) > 0:
            print(l[-1])
        else:
            print(-1)