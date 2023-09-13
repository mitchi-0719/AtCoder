# AC

s = [input() for _ in range(8)]
chars = ["a", "b", "c", "d", "e", "f", "g", "h"]

for i in range(8):
    for j in range(8):
        if s[i][j] == "*":
            ans = str(chars[j]) + str(8 - i)
            print(ans)
            exit()