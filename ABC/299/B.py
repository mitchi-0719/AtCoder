n, t = map(int, input().split())
idx = [i+1 for i in range(n)]
c = list(map(int, input().split()))
r = list(map(int, input().split()))

sorted_r, sorted_c, sorted_i = zip(*sorted(zip(r, c, idx), reverse=True))

p1_c = c[0]
p1_r = r[0]

max_i = 0

for i in range(n):
    if sorted_c[i] == t:
        print(sorted_i[i])
        exit()
    if sorted_c[i] == p1_c and max_i == 0:
        max_i = sorted_i[i]

print(max_i)