def solution(n):
    if n == 3:
        return ['***', '* *', '***']
    
    s = solution(n//3)
    
    result = []
    for i in range(n//3):
        result.append(s[i] * 3)
    for i in range(n//3):
        result.append(s[i] + ' '*(n//3) + s[i])
    for i in range(n//3):
        result.append(s[i] * 3)
    return result

n = int(input())
s = solution(n)

for e in s:
    print(e)