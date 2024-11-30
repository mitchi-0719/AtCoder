n, d = map(int, input().split())
s = input()[::-1].replace("@", ".", d)[::-1]
print(s)
