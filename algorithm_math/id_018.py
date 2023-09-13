n = int(input())
a = list(map(int, input().split()))

dic = {100:0, 200:0, 300:0, 400:0}

for i in a:
    dic[i] = dic[i] +1

print(dic[100]*dic[400] + dic[200]*dic[300])