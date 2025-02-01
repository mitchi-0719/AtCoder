d = input()
dir = ["N", "E", "W", "S"]

for di in d:
    d_idx = dir.index(di)
    print(dir[-(d_idx + 1)], end="")
