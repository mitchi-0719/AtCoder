n, k = map(int, input().split())
s = input()

i = 0
ans = 0
while i < n - k + 1:
    if s[i : i + k] == "O" * k:
        ans += 1
        i += k
    else:
        i += 1

print(ans)
