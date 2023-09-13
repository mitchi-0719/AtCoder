n = int(input())
w = list(map(str, input().split()))

a = ["and", "not", "that", "the", "you"]

for i in a:
    if i in w:
        print("Yes")
        exit()

print("No")