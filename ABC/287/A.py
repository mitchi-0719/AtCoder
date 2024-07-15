n = int(input())
s = [input() for _ in range(n)]

print("Yes" if (n + 1) // 2 <= s.count("For") else "No")
