n, a, b = map(int, input().split())
s = input()

def isPalindrome(st):
    count = 0
    for i in range(len(st)//2):
        if s[i] == s[len(st)-1-i]:
            count += 1
    return count

min = b * n//2
move_count = 0
match_count = 0

for i in range(n):
    match_count = isPalindrome(s)

    buffer = (n//2 - match_count) * b + move_count * a
    if buffer < min:
        min = buffer
    s = s[1:] + s[0]
    move_count += 1

print(min)