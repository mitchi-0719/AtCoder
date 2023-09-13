#正解

k = int(input())

hour = 21
hour += int(k / 60)

if hour >= 24:
    hour -= 24

minute = k % 60
h = str(hour)
m = str(minute)
if len(m) == 1:
    m = "0" + m
if len(h) == 1:
    h = "0" + h

print(h + ":" + m)