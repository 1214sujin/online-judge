A = []

for i in range(9):
    A.append(list(map(int, input().split())))

maxX = -1
maxY = -1
maxV = -1
for i in range(9):
    tmp = max(A[i])
    if tmp > maxV:
        maxV = tmp
        maxX = i
        maxY = A[i].index(maxV)

print(maxV)
print(maxX+1, maxY+1)