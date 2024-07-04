n = int(input())
a = list(map(int, input().split()))
m = max(a)
print(max([ai for ai in a if m != ai]))
