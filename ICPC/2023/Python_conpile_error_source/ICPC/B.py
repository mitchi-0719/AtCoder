def search(x, changed, i, now, goal, n):
    # print(i, n)
    # print(x)
    
    if i == n:
        if now == goal:
            return "OK"
        elif not changed and abs(now - goal) == 1:
            if now + 1 == goal:
                return str(now) + " " + str(i)
            else:
                return str(now - 1) + " " + str(i)
        else:
            return "NG"
    # print(x[i])
    
    if (x[i] == now):
        now += 1
    elif (x[i] == now - 1):
        now -= 1
    
    i += 1
    
    center = search(x, changed, i, now, goal, n)
    if center == "OK":
        return "OK"
    if not changed:
        left = search(x, True, i, now - 1, goal, n)
        if left == "OK":
            return str(now - 1) + " " + str(i) 
        right = search(x, True, i, now + 1, goal, n)
        if right == "OK":
            return str(now) + " " + str(i)
    return center
    
# import copy

while True:
    n, m, p, q = map(int, input().split())
    if (n == m == p == q == 0):
        break
    x = list(map(int, input().split()))

    # print(search(x, False, 0, p, q, m))
    center = search(x, False, 0, p, q, m)
    if center == "OK":
        print("OK")
        continue
    left = search(x, False, 0, p - 1, q, m)
    if left == "OK":
        print(str(p - 1) + " " + str(0))
        continue
    right = search(x, False, 0, p + 1, q, m)
    if right == "OK":
        print(str(p) + " " + str(0))
        continue
    print(center)


    # now = p
    # for i in range(m):
    #     if (x[i] == now):
    #         now += 1
    #     elif (x[i] == now - 1):
    #         now -= 1
    # if now == q:
    #     print("OK")
    # else:
    #     for k in range(n):
    #         for j in range(m):
    #             _x = j
    #             _y = k
    #             change_x = copy.deepcopy(x)
    #             change_x.insert(_y, _x)
    #             print(change_x)
    #             now = p
    #             for i in range(m + 1):
    #                 if (change_x[i] == now):
    #                     now += 1
    #                 elif (change_x[i] == now - 1):
    #                     now -= 1
    #             if now == q:
    #                 print(_x, _y)
    #                 break
    #     print("NG")
        