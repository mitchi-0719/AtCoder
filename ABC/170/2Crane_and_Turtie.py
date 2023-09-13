#正解
x, y = map(int, input().split())
z = 0

while True:
	a = x - z
	ans = a * 2 + z * 4
	if ans == y:
		print("Yes")
		break
	z += 1

	if z > x:
		print("No")
		break
