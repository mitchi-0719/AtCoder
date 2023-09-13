# AC

n, m = map(int, input().split())

diff = [set([]) for _ in range(n)]
nums = [set([i+1 for i in range(n) if i != j]) for j in range(n)]

for i in range(m):
    a = list(map(int, input().split()))
    for j in range(n):
        idx = a.index(j+1)
        if idx - 1 >= 0:
            diff[j].add(a[idx-1])
        if idx + 1 < n:
            diff[j].add(a[idx+1])


diff_count = 0
for i in range(n):
    diff_count += len(nums[i] - diff[i])

print(diff_count//2)