s = input()

m = 1

for i in range(len(s)):
    for j in range(i+1, len(s)+1):
        sub_s = s[i:j]
        mid = len(sub_s)//2

        if len(sub_s) % 2 == 0:
            if sub_s[0:mid] == sub_s[mid:len(sub_s)][::-1]:
                m = max(m, len(sub_s))
        else:
            if sub_s[0:mid] == sub_s[mid+1:len(sub_s)][::-1]:
                m = max(m, len(sub_s))

print(m)