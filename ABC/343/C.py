import math


def judge(m):
    m = str(m)
    for i in range(len(m)):

        if m[i] != m[-(i + 1)]:
            return False

    return True


n = int(input())


for i in range(10**6, -1, -1):
    cube = i**3
    if cube <= n and judge(cube):
        print(cube)
        exit()
