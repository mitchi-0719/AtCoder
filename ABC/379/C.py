n, m = map(int, input().split())
x = list(map(int, input().split()))
a = list(map(int, input().split()))
xa = zip(x, a)
xa = sorted(xa, key=lambda x: x[0], reverse=True)

ans = 0
fin = n + 1

for i in range(m):
    xi, ai = xa[i]
    dist = fin - xi
    if dist < ai:
        print(-1)
        exit()

    ans += (dist * (dist - 1)) // 2 - ((dist - ai) * ((dist - ai) - 1)) // 2
    fin -= ai

print(ans if fin == 1 else -1)
