from collections import defaultdict

s = list(input())
t = list(input())
n = len(s)
at = set(["a", "t", "c", "o", "d", "e", "r"])

ds = defaultdict(int)
dt = defaultdict(int)

for i in range(n):
    ds[s[i]] += 1
    dt[t[i]] += 1

s_at = s.count("@")
t_at = t.count("@")

for i in range(n):
    if s[i] != "@" and dt[s[i]] != 0:
        dt[s[i]] -= 1

    if t[i] != "@" and ds[t[i]] != 0:
        ds[t[i]] -= 1

s_rest = 0
t_rest = 0
judge = True

for k, v in ds.items():
    if k != "@" and k not in at and v != 0:
        judge = False
        break

    if k != "@":
        s_rest += v

for k, v in dt.items():
    if not judge:
        break

    if k != "@" and k not in at and v != 0:
        judge = False
        break

    if k != "@":
        t_rest += v

if judge and s_rest <= t_at and t_rest <= s_at:
    print("Yes")
else:
    print("No")
