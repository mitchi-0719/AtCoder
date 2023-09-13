# TLE

n, x = map(int, input().split())
a = list(map(int, input().split()))

a = dict(a)
n = len(a)
print(a)

# if x == 0:
#     print("Yes")
#     exit()

# for i in range(n):
#     div1 = x + a[i]
#     div2 = a[i] - x
#     if div1 in a or div2 in a:
#         print("Yes")
#         exit()

print("No")