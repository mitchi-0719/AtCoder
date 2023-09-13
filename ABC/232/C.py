n, m = map(int, input().split())

graph_1 = [[0 for i in range(n)] for j in range(n)]
graph_2 = [[0 for i in range(n)] for j in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    graph_1[a-1][b-1] = 1
    graph_1[b-1][a-1] = 1

for i in range(m):
    a, b = map(int, input().split())
    graph_2[a-1][b-1] = 1
    graph_2[b-1][a-1] = 1

g_cnt1 = []
g_cnt2 = []

for i in range(n):
    g_cnt1.append(graph_1[i].count(1))
    g_cnt2.append(graph_2[i].count(1))

if sorted(g_cnt1) == sorted(g_cnt2):
    print("Yes")
else:
    print("No")

