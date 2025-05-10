from collections import defaultdict
from pprint import pprint

while True:
    n = int(input())
    if n == 0:
        exit()
    s = [input() for _ in range(n)]
    s_dict = defaultdict(int)

    for _s in s:
        s_dict[_s] += 1
        for j in range(1, len(_s)):
            for k in range(1, len(_s)):
                if len(_s) - j - k <= 0:
                    break
                new_s = f"{_s[:j]}{len(_s) - j - k}{_s[len(_s)-k:]}"
                s_dict[new_s] += 1

    ans = 0
    for i, _s in enumerate(s):
        temp = _s
        omit_cnt = 0
        for j in range(1, len(_s)):
            for k in range(1, len(_s)):
                if len(_s) - j - k <= 0:
                    break
                new_s = f"{_s[:j]}{len(_s) - j - k}{_s[len(_s)-k:]}"
                if s_dict[new_s] == 1 and omit_cnt < len(_s) - j - k:
                    temp = new_s
                    omit_cnt = len(_s) - j - k
        ans += omit_cnt

    print(ans)
