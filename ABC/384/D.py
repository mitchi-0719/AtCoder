from itertools import accumulate

n, s = map(int, input().split())
a = list(map(int, input().split()))
a_sum = sum(a)
s %= a_sum

acc = list(accumulate(a + a))

right = 1
for left in range(n):

    while right < n * 2 and acc[right] - acc[left] <= s:
        right += 1
        if acc[right] - acc[left] == s:
            print("Yes")
            exit()

    if right == left:
        right += 1


print("No")
