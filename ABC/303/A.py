# AC

n = int(input())
s = input()
t = input()

s = s.replace("1", "l")
s = s.replace("0", "o")
t = t.replace("1", "l")
t = t.replace("0", "o")

sim_count = 0
for i, j in zip(s, t):
    if i == j:
        sim_count += 1

if len(s) == sim_count:
    print("Yes")
else:
    print("No")