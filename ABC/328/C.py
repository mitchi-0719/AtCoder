n, q = map(int, input().split())
s = input()

for i in range(q):
    l, r = map(int, input().split())

    part_s = s[l - 1 : r]
    ans = 0
    for j in range(len(part_s) - 1):
        ans += 1 if part_s[j] == part_s[j + 1] else 0
    print(ans)
