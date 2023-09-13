data_cnt = int(input())
ans = []

while data_cnt != 0:
    cnt = 0
    nums = list(map(int, input().split()))

    for i in range(1, data_cnt-1):
        if nums[i-1] < nums[i] and nums[i+1] < nums[i]:
            cnt += 1
    ans.append(cnt)
    data_cnt = int(input())
else:
    for i in ans:
        print(i)