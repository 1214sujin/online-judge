import sys

def solution(a, b, c):
    a, b, c = sorted([a, b, c])
    if c>a and c>b:
        if c >= a+b: return 'Invalid'
    
    if a==c:
        return 'Equilateral'
    elif a==b:
        return 'Isosceles'
    elif b==c:
        return 'Isosceles'
    else:
        return 'Scalene'

while True:
    a, b, c = map(int, sys.stdin.readline().split())
    if a==0 and b==0 and c==0:
        break
    print(solution(a, b, c))