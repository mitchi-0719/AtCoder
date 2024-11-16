n, k = map(int, input().split())
s = input()
k -= 1
block = []
start = -1

for i in range(n):
    if s[i] == "1" and start == -1:
        start = i
    elif start != -1 and s[i] == "0":
        block.append((start, i - 1, i - start))
        start = -1

if start != -1:
    block.append((start, n - 1, n - start))

s = s[: block[k][0]] + s[block[k][1] + 1 :]

print(s[: block[k - 1][1] + 1], end="")
print("1" * block[k][2], end="")
print(s[block[k - 1][1] + 1 :])
