import sys

n = int(sys.stdin.readline())
chats = [sys.stdin.readline().split()[0] for _ in range(n)]
dct = set()
s = 0

for i in range(n):
    if chats[i] == 'ENTER':
        s += len(dct)
        dct = set()
    else:
        dct.add(chats[i])

s += len(dct)
print(s)