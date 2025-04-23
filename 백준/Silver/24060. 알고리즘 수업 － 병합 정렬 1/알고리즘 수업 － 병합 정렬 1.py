import sys

n, k = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
cnt = 0

def merge(arr, p, q, r):
    global cnt
    i = p
    j = q
    tmp = []
    while i < q and j < r:
        if arr[i] <= arr[j]:
            tmp.append(arr[i])
            i += 1
        else:
            tmp.append(arr[j])
            j += 1
    if i < q:
        tmp.extend(arr[i:q])
    elif j < r:
        tmp.extend(arr[j:r])

    t = 0
    for i in range(p, r):
        cnt += 1
        if cnt == k:
            return tmp[t]
        arr[i] = tmp[t]
        t += 1
    return -1

def merge_sort(arr, p, r):
    if p+1 < r:
        q = (p+r+1)//2
        answer1 = max(merge_sort(arr, p, q), merge_sort(arr, q, r))
        answer2 = merge(arr, p, q, r)
        return max(answer1, answer2)
    return -1

answer = merge_sort(arr, 0, n)
print(answer)