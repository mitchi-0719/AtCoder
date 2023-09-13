import math

divs = []

def is_prime(n):
    i = 2
    while i <= math.sqrt(n):
        if n % i == 0:
            return False, i
        i += 1
    return True, 0

def prime_factorization(n):
    judge, i = is_prime(n)
    if judge:
        divs.append(n)
    else:
        prime_factorization(int(n/i))
        prime_factorization(i)


prime_factorization(int(input()))
divs = sorted(divs)
for i in divs:
    print(i, end=" ")