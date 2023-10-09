x = int(input())
li = list(map(int, input().split()))


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


print(binary_search(x, li))
