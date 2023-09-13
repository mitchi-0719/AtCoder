n = int(input())

books = []

for i in range(n):
    b = list(map(int, input().split()))
    books.append(b[1:])

