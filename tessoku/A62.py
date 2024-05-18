n, m = map(int, input().split())

true_s = "The graph is connected."
false_s = "The graph is not connected."

g = [[] for i in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

s = 1
stack = []
visit = [False for _ in range(n + 1)]

stack.append(s)
while len(stack) != 0:
    node = stack.pop()
    visit[node] = True
    for i in g[node]:
        if not visit[i]:
            stack.append(i)
            visit[i] = True

for i in range(1, n + 1):
    if not visit[i]:
        print(false_s)
        exit()

print(true_s)
