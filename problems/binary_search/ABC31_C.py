N, M = map(int, input().split())

a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())))

def binary_search(x, arr):
    low = 0
    high = len(arr)
    while low < high:
        mid = (low + high) // 2
        if arr[mid] < x:
            low = mid + 1
        else:
            high = mid
    return low

low = 10**10

for i in range(N):
    idx = binary_search(a[i], b)
    if i + 1 >= M - idx:
        low = min(low, a[i])
        break

for i in range(M):
    idx = binary_search(b[i] + 1, a)
    if M - i - 1 <= idx:
        low = min(low, b[i] + 1)
        break


print(low)