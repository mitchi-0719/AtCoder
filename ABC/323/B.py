n = int(input())
win = [input().count("o") for _ in range(n)]
idx = [i + 1 for i in range(n)]
win, idx = zip(*sorted(zip(win, idx), reverse=True, key=lambda x: (x[0], -x[1])))
print(*idx)
