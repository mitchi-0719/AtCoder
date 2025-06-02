m = int(input())

for _ in range(m):
    s = input()
    l = len(s)
    ans = set()

    for i in range(1, l):
        s1 = s[:i]
        s2 = s[i:]

        ans.add(s1 + s2)
        ans.add(s1[::-1] + s2)
        ans.add(s1 + s2[::-1])
        ans.add(s1[::-1] + s2[::-1])

        ans.add(s2 + s1)
        ans.add(s2 + s1[::-1])
        ans.add(s2[::-1] + s1)
        ans.add(s2[::-1] + s1[::-1])

    print(len(ans))
