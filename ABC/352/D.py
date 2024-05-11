n, k = map(int, input().split())
p = list(map(int, input().split()))

idx = [i + 1 for i in range(n)]

p, idx = zip(*sorted(zip(p, idx)))


min_diff = float("inf")
for i in range(n - k):
    sub_arr = idx[i : i + k]
    min_diff = min(min_diff, max(sub_arr) - min(sub_arr))

print(min_diff)
