n = int(input())
s = input()

idx = [i for i in range(n) if s[i] == "1"]
idx_n = len(idx)
mid = idx_n // 2
mid_num = idx[mid]

ans = 0
for i in range(idx_n):
    ans += max(0, abs(mid_num - idx[i]) - 1)

print(ans)
