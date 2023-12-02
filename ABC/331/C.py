from itertools import groupby

n = int(input())
a = list(map(int, input().split()))

a_sort = sorted(a, reverse=True)
a_run_length = [(k, len(list(g))) for k, g in groupby(a_sort)]
sum_dist = {}

prev = 0
for i in range(len(a_run_length)):
    if i == 0:
        sum_dist[a_run_length[i][0]] = 0
        prev = 0
    else:
        sum_dist[a_run_length[i][0]] = (
            prev + a_run_length[i - 1][0] * a_run_length[i - 1][1]
        )
        prev = sum_dist[a_run_length[i][0]]

for i in a:
    print(sum_dist[i], end=" ")
