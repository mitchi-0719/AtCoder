n = int(input())
x, y = 0, 0

for i in range(n):
    xi, yi = map(int, input().split())
    x += xi
    y += yi

print("Draw" if x == y else "Takahashi" if x > y else "Aoki")
