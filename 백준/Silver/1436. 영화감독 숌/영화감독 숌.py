n = int(input())
i = 0
cnt = 0
while True:
    i += 1
    if str(i).find('666') != -1:
        cnt += 1
        if cnt == n:
            print(i)
            break