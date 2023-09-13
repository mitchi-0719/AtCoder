n = int(input())

def func(num):
    if num == 1:
        return 2
    elif num == 0:
        return 1
    else:
        return func(int(num/2)) + func(int(num/3))

print(func(n))