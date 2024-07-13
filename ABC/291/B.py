n = int(input())
x = sorted(list(map(int, input().split())))

print(sum(x[n : 4 * n]) / (3 * n))
