n = int(input())
s = input()
w = list(map(int, input().split()))

w, s = zip(*sorted(zip(w, s)))

if len(set(s)) == 1:
    print(n)
    exit()

adult_cnt = s.count("1")
child_cnt = n - adult_cnt

f_ch_cnt = child_cnt
f_ad_cnt = 0
max_cnt = 0

for i in range(1, n):
    if s[-i] == "0":
        f_ch_cnt -= 1
    else:
        f_ad_cnt += 1
    max_cnt = max(f_ch_cnt + f_ad_cnt, max_cnt)

print(max_cnt)