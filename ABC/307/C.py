def arr_input(arr, idx):
    H, W = map(int, input().split())
    h.append(H)
    w.append(W)

    for i in range(h[idx]):
        arr.append(input())

def remove_null_line(arr):
    r = len(arr)
    c = len(arr[0])

    not_remove_top = True
    not_remove_bottom = True
    remove_cnt = 0
    i = 0

    # 列方向の削除
    while i < r and not_remove_top and not_remove_bottom:
        print("c", r, remove_cnt, i, arr)
        if set(arr[i-remove_cnt]) == {"."} and not_remove_top:
            arr.remove(arr[i-remove_cnt])
            remove_cnt += 1
            print("a", r, remove_cnt, i, arr)
        else:
            not_remove_top = False

        if set(arr[r - i-remove_cnt-1]) == {"."} and not_remove_bottom:
            arr.remove(arr[r - i-remove_cnt-1])
            print("b", r, remove_cnt, i, arr)
        else:
            not_remove_bottom = False
        i += 1

    find_start = False
    find_end = False

    for j in range(c):
        for k in range(r):
            

h = []
w = []
a = []
b = []
x = []

arr_input(a, 0)
arr_input(b, 1)
arr_input(x, 2)

remove_null_line(a)
remove_null_line(b)
remove_null_line(x)
print(a)
print(b)
print(x)