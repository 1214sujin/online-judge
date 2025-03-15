def print_perfect(n, 약수s):
    print(f'{n} = {약수s[0]}', end='')
    for a in 약수s[1:]:
        print(f' + {a}', end='')
    print()

n = int(input())
while n != -1:
    약수s = []
    for i in range(1, n):
        if n % i == 0:
            약수s.append(i)
    if sum(약수s) == n:
        print_perfect(n, 약수s)
    else:
        print(f'{n} is NOT perfect.')
    
    n = int(input())