n = int(input())

def judge(n):
    n_list = list(str(n))
    return int(n_list[0]) * int(n_list[1]) == int(n_list[2])

i = 0
while True:
    if judge(n+i):
        print(n+i)
        exit()
    i += 1