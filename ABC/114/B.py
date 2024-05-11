# AC

s = input()

ans = 753
diff = float("inf")
for i in range(len(s) - 2):
    diff = min(diff, abs(ans - int(s[i : i + 3])))

print(diff)
