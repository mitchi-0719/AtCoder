n = int(input())
ns = str(n)


def is_kaibun(s):
    return s == s[::-1]


cnt = 0
for i in range(len(ns)):
    if ns[::-1][i] != "0":
        break
    cnt += 1

print("Yes" if is_kaibun(ns[::-1][cnt:]) else "No")
