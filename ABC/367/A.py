a, b, c = map(int, input().split())

if b < c:
    print("Yes" if not b < a < c else "No")
else:
    print("Yes" if c <= a <= b else "No")
