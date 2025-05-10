def solve(w):
    for i in range(len(w)):
        if judge(w[i:]):
            print(i + 1)
            return


def judge(w):
    phrase = [5, 7, 5, 7, 7]
    total = 0
    i = 0
    for word in w:
        total += len(word)
        if phrase[i] == total:
            total = 0
            i += 1
        elif phrase[i] < total:
            return False

        if i == 5:
            return True


while True:
    n = int(input())
    if n == 0:
        exit()
    w = [input() for _ in range(n)]
    solve(w)
