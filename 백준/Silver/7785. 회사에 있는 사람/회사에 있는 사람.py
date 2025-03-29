import sys

n = int(sys.stdin.readline())
member_set = set()
for _ in range(n):
    name, state = sys.stdin.readline().split()
    if state == 'enter':
        member_set.add(name)
    elif state == 'leave':
        member_set.remove(name)

members = list(member_set)
members.sort(reverse=True)

for m in members:
    print(m)