N = int(input())


def calc(ans, L, R):
    if L == N // 2:
        for i in range(len(ans)):
            if ans[i] == ".":
                ans[i] = ")"
                L += 1
    elif R == N // 2:
        for i in range(len(ans)):
            if ans[i] == ".":
                ans[i] = "("
                R += 1
    return L, R


ans = ["."] * N
candidate = [0]
i = 0
ans[0] = "("
ans[-1] = ")"
L_cnt = 1
R_cnt = 1
while i < N - 1:
    print("?", i+1, i + 2)
    ret = int(input())
    if ret:
        ans[i] = "("
        ans[i + 1] = ")"
        L_cnt += 1
        R_cnt += 1
        i += 2
        continue
    elif ans[i] == "(":
        ans[i + 1] = "("
        L_cnt += 1
    if i == N - 2 and not ret:
        candidate.append(i + 1)
    candidate.append(i)
    i += 1

L_cnt, R_cnt = calc(ans, L_cnt, R_cnt)
if L_cnt + R_cnt == N:
    print("!","".join(ans))
    exit()

while candidate:
    M = len(candidate)
    skip = False
    for i in range(M - 1):
        if skip:
            skip = False
            continue
        L = candidate[i]
        R = candidate[i + 1]
        print("?", L+1, R+1)
        ret = int(input())
        if ret:
            if ans[L] == ".":
                L_cnt += 1
            if ans[L] == ".":
                R_cnt += 1
            ans[L] = "("
            ans[R] = ")"
            candidate.remove(L)
            candidate.remove(R)
            skip = True
        else:
            if ans[L] == "(":
                ans[R] = ")"
                R_cnt += 1
    L_cnt, R_cnt = calc(ans, L_cnt, R_cnt)

print("!","".join(ans))
