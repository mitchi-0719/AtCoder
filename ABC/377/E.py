# import math

# n, k = map(int, input().split())
# p = list(map(int, input().split()))
# c = int(math.log2(n))
# log = []

# for i in range(c):
#     new_p = []
#     for j in range(n):
#         new_p.append(p[p[j] - 1])
#     p = new_p
#     log.append(new_p)

# print(log)


from itertools import permutations


c = int(input())
p = permutations([i for i in range(c)])
k_max = -1
for _pi in p:
    pi = _pi
    k = -1
    # print("start", _pi)
    for i in range(5):
        new_p = []
        for j in range(c):
            new_p.append(pi[pi[j]])
        pi = new_p
        if [*pi] == [*_pi]:
            k = i
            break
    # print(k, pi)
    k_max = max(k, k_max)

print(k_max)
