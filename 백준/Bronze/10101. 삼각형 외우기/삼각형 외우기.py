import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())

if a+b+c == 180:
    if a==b: 
        if a==c:
            print('Equilateral')
        else:
            print('Isosceles')
    elif b==c:
        print('Isosceles')
    elif a==c:
        print('Isosceles')
    else:
        print('Scalene')
else:
    print('Error')