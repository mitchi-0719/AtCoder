n, x, y, z = map(int, input().split())

print("Yes" if x < z < y or x > z > y else "No")
