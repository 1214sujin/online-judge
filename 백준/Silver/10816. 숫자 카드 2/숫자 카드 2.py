import sys

n = int(sys.stdin.readline())
sg = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))
cards_dict = {int(e):0 for e in cards}

for e in sg:
    if e in cards_dict.keys():
        cards_dict[e] += 1
for c in cards:
    print(cards_dict[c], end=' ')