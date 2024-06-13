def base_n(num_10, n):
    str_n = ""
    while num_10:
        if num_10 % n >= 10:
            return -1
        str_n += str(num_10 % n)
        num_10 //= n
    return str_n[::-1]


n = int(input())
if n == 1:
    print(0)
    exit()

nums = ["0", "2", "4", "6", "8"]
five_n = base_n(n - 1, 5)
ans = ""
for f in five_n:
    ans += nums[int(f)]

print(ans)
