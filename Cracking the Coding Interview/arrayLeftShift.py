def array_left_rotation(a, n, k):
    if n == 0:
        return []
    k %= n
    for i in range(k):
        a.append(a[0])
        a.pop(0)
    return a

n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
answer = array_left_rotation(a, n, k)
print(*answer, sep=' ')