n = int(input())
a = list(map(int, input().split()))

go = []
come = [[] for _ in range(n)]

for i in range(n):
    go.append([i+1, a[i]])
    come[a[i]-1].append(i+1)


print(go)
print(come)