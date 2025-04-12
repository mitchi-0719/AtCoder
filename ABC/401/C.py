mod = 10**9

n, k = map(int, input().split())
arr = [0 for _ in range(n + 1)]
s = k

for i in range(n + 1):
    if i < k:
        arr[i] = 1
    else:
        arr[i] = s % mod
        s += arr[i]
        s -= arr[i - k]

print(arr[-1])
