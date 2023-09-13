n = int(input())
ans = []

while n != 0:
    a = list(map(int, input().split()))
    ans.append(max(a))
    n = int(input())

for i in range(len(ans)):
    print(ans[i])