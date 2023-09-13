while True:
    n = int(input())
    if n == 0:
        break
    s = list(input())
    
    l = []
    for k in range(len(s)):
        if (s[k] == 'o'):
            l.append(k)
    l.remove(0)
    print(l)