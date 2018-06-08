import math
import time
def sieve(n):
    """find all prime numbers up to n, O(n*log(log(n)))"""
    sieve = [True for l in range(n + 1)]
    sieve[0:1] = [False, False]
    # heuristic to save some time - takes into account factors of n are < sqrt(n)
    for j in range(2, math.ceil(math.sqrt(n)) + 1):
        if sieve[j]:
            for i in range(2 * j, n + 1, j):
                sieve[i] = False

    # formatting into an array
    primes = []
    for i in range(2, n + 1):
        if sieve[i]:
            primes.append(i)
    return primes