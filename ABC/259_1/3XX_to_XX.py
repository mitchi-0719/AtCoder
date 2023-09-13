s = input()
t = input()

s_char = []
s_cnt = []

t_char = []
t_cnt = []

def change_str(arr, new_arr, arr_cnt):
    i = 0
    j = 0
    while i < len(arr):
        new_arr.append(arr[i])
        arr_cnt.append(1)
        i += 1

        while i < len(arr) and new_arr[j] == arr[i]:
            arr_cnt[j] += 1
            i += 1
        j += 1

change_str(s, s_char, s_cnt)
change_str(t, t_char, t_cnt)

if s_char != t_char:
    print("No")
    exit()
else:
    length = len(s_char)
    for i in range(length):
        if not(s_cnt[i] == t_cnt[i] or s_cnt[i] >= 2 and s_cnt[i] < t_cnt[i]):
            print("No")
            exit()
    print("Yes")