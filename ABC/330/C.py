import bisect

d = int(input())
ans = float("inf")
squares = []

for i in range(10**6):
    squares.append(i**2)

squares.append(float("inf"))

l = len(squares)
for i in range(10**6):
    square = i**2
    tmp = abs(square - d)
    idx = bisect.bisect(squares, tmp)
    ans = min(
        ans,
        abs(square + squares[idx] - d),
        abs(square + squares[idx - 1] - d),
        abs(square + squares[min(l - 1, idx + 1)] - d),
    )

print(len(ans))
