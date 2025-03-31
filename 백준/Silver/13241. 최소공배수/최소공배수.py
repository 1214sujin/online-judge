def 호제법(a, b):
    b, a = sorted([a, b])
    r = a%b
    if r==0:
        return b
    else:
        return 호제법(b, r)

def get공약수and몫(a, b):
    i = 2
    r = 호제법(a, b)
    return r, a//r, b//r

a, b = map(int, input().split())

공약수list = []
while True:
    공약수, a, b = get공약수and몫(a, b)
    if 공약수 == 1:
        break
    공약수list.append(공약수)
ans = a*b
for e in 공약수list:
    ans *= e
print(ans)