import random


# ループver
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


# 再帰ver
def recursion_binary_search(x, arr, l, r):
    m = (l + r) // 2
    if arr[m] == x:
        return m
    elif l > r:
        return -1
    elif x < arr[m]:
        return recursion_binary_search(x, arr, l, m - 1)
    else:
        return recursion_binary_search(x, arr, m + 1, r)


x = int(input("0 to 100："))
li = [random.randint(0, 100) for _ in range(10)]
li = sorted(list(set(li)))

print(li)
print(binary_search(x, li))
print(recursion_binary_search(x, li, 0, len(li)))
