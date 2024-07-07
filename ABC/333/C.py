from itertools import combinations

n = int(input())
nums = sorted([i % 12 for i in range(36)])

li = []
for i in range(12):
    li.append(int("1" * (i + 1)))

c = list(set(combinations(nums, 3)))
c_num = sorted([sum([li[v] for v in ci]) for ci in c])

print(c_num[n - 1])
