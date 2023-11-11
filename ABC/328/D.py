s = input()

while True:
    prev_s = s
    s = s.replace("ABC", "")
    if prev_s == s:
        break

print(s)
