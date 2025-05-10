def calc(s1, s2):
    return decode(encode(s1) + encode(s2))


def encode(s):
    obj = {
        "m": 1000,
        "c": 100,
        "x": 10,
        "i": 1,
    }

    i = 0
    temp = 1
    ans = 0

    while i < len(s):
        if s[i] in obj.keys():
            ans += temp * obj[s[i]]
            temp = 1
        else:
            temp = int(s[i])
        i += 1

    return ans


def decode(num):
    arr = ["m", "c", "x", "i"]
    s_num = (4 - len(str(num))) * "0" + str(num)
    ans = ""

    for i, s in enumerate(s_num):
        if s == "1":
            ans += arr[i]
        elif s != "0":
            ans += s + arr[i]
    return ans


n = int(input())
for i in range(n):
    s1, s2 = input().split()
    print(calc(s1, s2))
