sub = "wbwbwwbwbwbw" * 100

w, b = map(int, input().split())


for i in range(len(sub) - (w + b)):
    if w == sub[i : i + w + b].count("w") and b == sub[i : i + w + b].count("b"):
        print("Yes")
        exit()

print("No")
