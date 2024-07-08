nums = [0] + [i**i for i in range(1, 16)]

b = int(input())
print(-1 if b not in nums else nums.index(b))
