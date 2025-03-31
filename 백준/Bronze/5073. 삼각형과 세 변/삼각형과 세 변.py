import sys

def solution(a, b, c):
    if a>b and a>c:
        if a >= b+c: return 'Invalid'
    if b>a and b>c:
        if b >= a+c: return 'Invalid'
    if c>a and c>b:
        if c >= a+b: return 'Invalid'
    
    if a==b: 
        if a==c:
            return 'Equilateral'
        else:
            return 'Isosceles'
    elif b==c:
        return 'Isosceles'
    elif a==c:
        return 'Isosceles'
    else:
        return 'Scalene'

while True:
    a, b, c = map(int, sys.stdin.readline().split())
    if a==0 and b==0 and c==0:
        break
    print(solution(a, b, c))