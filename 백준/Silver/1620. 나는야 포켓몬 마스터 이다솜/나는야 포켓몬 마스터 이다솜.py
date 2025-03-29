n, m = map(int, input().split())
pkm_number = {i+1:input() for i in range(n)}
pkm_dict = {value:key for key, value in pkm_number.items()}

for i in range(m):
    q = input()
    if ord(q[0]) >= 48 and ord(q[0]) <= 57:
        print(pkm_number.get(int(q)))
    else:
        print(pkm_dict.get(q))