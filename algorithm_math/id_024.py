n = int(input())

expect = 0
for i in range(n):
    p, q = map(int, input().split())
    expect += q/p

print(expect)