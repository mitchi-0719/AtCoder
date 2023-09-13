#正解

l, r = map(int, input().split())
words = ["a", "t", "c", "o", "d", "e", "r"]

for i in range(l - 1, r):
    print(words[i], end="")