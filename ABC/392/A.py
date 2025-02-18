from itertools import permutations

a = list(map(int, input().split()))

for ap in permutations(a, 3):
    if ap[0] * ap[1] == ap[2]:
        print("Yes")
        exit()

print("No")
