def get_prime(n):
    sieve = [True] * (n + 1)
    i = 2
    while i * i <= n:
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
        i += 1
    return [i for i in range(2, n + 1) if sieve[i]]
