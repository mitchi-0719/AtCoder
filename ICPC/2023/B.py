def search(arr):
    now = p
    for i in range(len(arr)):
        if arr[i] == now:
            now += 1
        elif arr[i]+1 == now:
            now -= 1
    if now == q:
        return "OK"
    else:
        return "NO"

n, m, p, q = map(int, input().split())

ans = []

while True:
    if n == m == p == q == 0:
        break

    x = list(map(int, input().split()))

    now = p
    for i in range(len(x)):
        if x[i] == now:
            now += 1
        elif x[i]+1 == now:
            now -= 1

    if now == q:
        a = "OK"
    else:
        a = "NO"
    ans.append(a)

    n, m, p, q = map(int, input().split())

for i in range(len(ans)):
    print(ans[i])