"""
10進数をn進数に変換する関数
"""


def base_n(num_10, n):
    str_n = ""
    while num_10 > 0:
        if num_10 % n >= 10:
            return -1
        str_n = str(num_10 % n) + str_n
        num_10 //= n
    return str_n


"""
n進数を10進数に変換する関数。
"""


def base_10(num_n, n):
    num_10 = 0
    for s in str(num_n):
        num_10 *= n
        num_10 += int(s)
    return num_10
