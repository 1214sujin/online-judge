t = input().split()
for i in range(3):
    t[i] = int(t[i])

if t[1] >= t[2]:
    print("-1")
else:
    x = t[0] / (t[2] - t[1])
    print(int(x)+1)