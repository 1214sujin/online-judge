num = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]    #0 1 2 3 4 5 6 7 8 9
a = int(input())
b = int(input())
c = int(input())
d = str(a*b*c)
for i in range(len(d)):
    e = d[i]
    num[int(e)] += 1
for i in range(10):
    print(num[i])