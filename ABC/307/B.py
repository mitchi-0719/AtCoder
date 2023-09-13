n = int(input())
s = []

for i in range(n):
    s.append(input())

def judge_palindrome(s):
    for i in range(len(s)//2):
        if s[i] != s[len(s)-i-1]:
            return False
    return True

for i in range(n):
    for j in range(n):
        if i != j:
            if judge_palindrome(s[i] + s[j]):
                print("Yes")
                exit()

print("No")