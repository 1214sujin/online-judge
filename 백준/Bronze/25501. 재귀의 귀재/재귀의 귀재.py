def recursion(s, p, cnt):
    cnt += 1
    if p >= len(s)//2:
        return 1, cnt
    elif s[p] != s[-1-p]:
        return 0, cnt
    else:
        r, cnt = recursion(s, p+1, cnt)
        return r, cnt

def isPalindrome(s, cnt):
    return recursion(s, 0, cnt)

n = int(input())

for _ in range(n):
    s = input()
    isP, count = isPalindrome(s, 0)
    print(isP, count)