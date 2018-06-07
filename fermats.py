# probabilistic based on Fermat's Little Theorem:
# if n is prime, for every A within 1 to n-1,
# A^(n-1) ≡ 1 (mod n)
# in other terms, A^(n-1) % n = 1
#
# .00000087412 chance of error, based on the fact that
# there are only 21853 pseudoprimes base 2 that are less than 2.5 * (10**10)

# n is the number to test, k is the iterations of the test where a larger k
# provides a smaller margin of error

import random
import math
def prime(n, k=1):

    if n < 2: return False
    
    while k > 0:
        a = 2 + math.floor(random.random() * (n - 2))
        print(a)
        if a**(n-1) % n != 1:
            return False
        k -= 1
    return True

print(prime(332))