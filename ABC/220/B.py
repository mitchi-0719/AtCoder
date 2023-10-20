k = int(input())
a, b = map(int, input().split())


def calc(n, k):
    ans = 0
    for i, val in enumerate(reversed(str(n))):
        ans += int(val) * (k**i)
    return ans


print(calc(a, k) * calc(b, k))
