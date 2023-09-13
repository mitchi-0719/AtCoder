n, d = map(int, input().split())
s = []

for i in range(n):
    s.append(input())

def judge(idx):
    i = 0
    while i < n:
        if s[i][idx] != "o":
            return False
        i += 1
    return True

m = 0
length = 0
for i in range(d):
    if judge(i):
        length += 1
    else:
        m = max(m, length)
        length = 0

m = max(m, length)
print(m)