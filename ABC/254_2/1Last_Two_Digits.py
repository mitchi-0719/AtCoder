#正解

n = int(input())

dig = str(n % 100)

if len(dig) == 1:
    dig = "0" + dig

print(dig)