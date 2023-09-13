l, r = map(int, input().split())
s = input()

if l == 1 and r == len(s):
    print(s[::-1])
else:
    print(s[:l-1] + s[r-1:l-2:-1] + s[r:])