import math
def sieve(n):
    """find all prime numbers up to n"""
    sieve = [True for l in range(n + 1)]
    sieve[0:1] = [False, False]
    for j in range(2, math.ceil(math.sqrt(n)) + 1):
        if sieve[j]:
            for i in range(2 * j, n + 1, j):
                sieve[i] = False
    primes = []
    for i in range(2, n + 1):
        if sieve[i]:
            primes.append(i)
    return primes
print(sieve(10000000))