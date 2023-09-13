#正解

s = input()

s_sort = sorted(s)

ans = ""
for i in s_sort:
    ans += i

print(ans)