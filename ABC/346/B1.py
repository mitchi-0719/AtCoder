p = "wbwbwwbwbwbw" * 30

w, b = map(int, input().split())
for i in range(len(p) - (w + b)):
    sub = p[i : i + w + b]
    if sub.count("w") == w and sub.count("b") == b:
        print("Yes")
        exit()

print("No")
