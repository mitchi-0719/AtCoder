from itertools import accumulate
import math


n, m = map(int, input().split())

l = list(map(int, input().split()))
l = [li + 1 for li in l]
l_acc = list(accumulate(l))
length = sum(l) - m
w = max(*l, math.ceil(length // m)) - 1
