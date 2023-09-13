def m_dist(x1, y1, x2, y2):
    return abs(x1-x2)+abs(y1-y2)

def check(n, a):
    for i in range(n**2):
        for j in range(n**2):
            x1 = i//n
            y1 = x1*n + i%n
            x2 = j//n
            y2 = x1*n + j%n
            m_dist(x1, y1, x2, y2)
    

n = int(input())
while n!=0:
    a = [list(map(int,input().split())) for i in range(n)]
    # original 2 pair dist dict
    near_dict = {}
    for i in range(n):
        for j in range(n):
            obj = []
            if i - 1 < 0:
                obj.append(a[i-1][j])
            if i + 1 > n:
                obj.append(a[i+1][j])
            if j - 1 < 0:
                obj.append(a[i][j-1])
            if j + 1 > n:
                obj.append(a[i][j+1])
           
            near_dict[a[i][j]] = obj
            print(near_dict)

    # sekigae
    # new_a = []
    # sekigae no check

    # print(a)
    n = int(input())

