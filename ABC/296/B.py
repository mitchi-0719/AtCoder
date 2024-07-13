c = ["a", "b", "c", "d", "e", "f", "g", "h"]
n = [8, 7, 6, 5, 4, 3, 2, 1]

for i in range(8):
    s = input()
    if "*" in s:
        j = s.index("*")
        if j != -1:
            print(f"{c[j]}{n[i]}")
            exit()
