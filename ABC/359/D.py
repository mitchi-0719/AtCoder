def isPalindrome(s, f, l):
    for i in range((l - f + 1) // 2):
        if s[i + f] != s[l - i]:
            return False

    return True


mod = 998244353

n, k = map(int, input().split())
s = list(input())

ans = 0
for i in range(n - k):
    if isPalindrome(s, i, i + k - 1):
        good = False
        break

print(ans % mod)
