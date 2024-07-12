n, m = map(int, input().split())
a = list(reversed(list(map(int, input().split()))))
c = list(reversed(list(map(int, input().split()))))

b = [0 for _ in range(m + 1)]


print(*list(reversed(b)))
