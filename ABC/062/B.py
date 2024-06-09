#AC
h, w = map(int, input().split())

a = [input() for _ in range(h)]

print("#"*(w+2))
for i in range(h):
    print("#", end="")
    print(a[i], end="")
    print("#")
print("#"*(w+2))