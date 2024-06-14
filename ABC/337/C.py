n = int(input())
a = list(map(int, input().split()))
dic = dict()

for i, ai in enumerate(a):
    dic[ai] = i

start = dic[-1]
ans = [start + 1]

for i in range(n - 1):
    next = dic[ans[i]]
    ans.append(next + 1)

print(*ans)
