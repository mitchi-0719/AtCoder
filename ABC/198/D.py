from itertools import permutations

ng = "UNSOLVABLE"
s1, s2, s3 = input(), input(), input()
num = [i for i in range(10)]

st_list = sorted(list(set([si for si in s1 + s2 + s3])))
st_cnt = len(st_list)

if st_cnt > 10:
    print(ng)
    exit()

for per in list(permutations(num, st_cnt)):
    n1 = int("".join([f"{per[st_list.index(si)]}" for si in s1]))
    n2 = int("".join([f"{per[st_list.index(si)]}" for si in s2]))
    n3 = int("".join([f"{per[st_list.index(si)]}" for si in s3]))

    if (
        [n1, n2, n3].count(0) == 0
        and [len(str(n1)), len(str(n2)), len(str(n3))] == [len(s1), len(s2), len(s3)]
        and n1 + n2 == n3
    ):
        print(n1)
        print(n2)
        print(n3)
        exit()

print(ng)
