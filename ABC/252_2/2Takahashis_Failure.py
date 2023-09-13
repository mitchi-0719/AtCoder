#正解

n, k = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

max_idx = [i for i, x in enumerate(A) if x == max(A)]

for i in max_idx:
    for j in B:
        if i == j - 1:
            print("Yes")
            exit()

print("No")