#不正解

n, q = map(int, input().split())
S = [input().split() for _ in range(q)]

follows = [["N" for __ in range(n)] for _ in range(n)]

for i in range(q):
    buffer = []
    log = [int(j)-1 for j in S[i]]
    if log[0] == 0:
        if log[1] != log[2]:
            follows[log[1]][log[2]] = "Y"
    elif log[0] == 1:   
        for j in range(n):
            if follows[j][log[1]] == "Y":
                buffer.append(j)
        for j in buffer:
            follows[log[1]][j] = "Y"
    else:
        for j in range(n):
            if follows[log[1]][j] == "Y":
                for k in range(n):
                    if follows[j][k] == "Y":
                        buffer.append(k)
        for j in buffer:
            follows[log[1]][j] = "Y"

for a in range(n):
    sentence = ""
    for j in range(n):
        sentence += follows[a][j]
    print(sentence)