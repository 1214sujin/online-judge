answer = []
def solution(now, target, number):
    if number == 1:
        answer.append((now, target))
        return target
    head_target = 6 - now - target
    solution(now, head_target, number-1)
    answer.append((now, target))
    solution(head_target, target, number-1)

n = int(input())

solution(1, 3, n)
print(len(answer))
for a in answer:
    print(a[0], a[1])