s = input()
괄호map = {'(': ')', '[': ']'}

while s != '.':
    stack = []
    answer = 'yes'
    for c in s:
        if c in 괄호map.keys():
            stack.append(c)
        elif c in 괄호map.values():
            if len(stack) > 0:
                _c = stack.pop()
                if 괄호map[_c] != c:
                    answer = 'no'
                    break
            else:
                answer = 'no'
                break
    if len(stack) > 0:
        answer = 'no'
    print(answer)
    s = input()