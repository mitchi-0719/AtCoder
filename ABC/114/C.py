# TLE

n = int(input())

ans = 0

i = 357
while i < n:
    if {"3", "5", "7"} == set(list(str(i))):
        ans += 1
    i += 1
    if i > 1000 and str(i)[-1] not in ["3", "5", "7"]:
        i += 1000

print(ans)
