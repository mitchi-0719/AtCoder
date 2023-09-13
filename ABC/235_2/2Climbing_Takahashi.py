#正解

n = int(input())
H = list(map(int, input().split()))

idx = 0
while idx < n - 1 and H[idx] < H[idx + 1]:
    idx += 1

print(H[idx])