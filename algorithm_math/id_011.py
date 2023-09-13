n = int(input())

for i in range(2, n+1):
    div_cnt = 0
    for j in range(1, i+1):
        div_cnt += 1 if i % j == 0 else 0
    if div_cnt == 2:
        print(i, end=" ")
    div_cnt = 0