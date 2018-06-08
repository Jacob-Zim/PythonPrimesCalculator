import math
import time
def prime_factors(n):
    arr = []

    # grab the factors of 2
    while n % 2 == 0:
        arr.append(2)
        n = n / 2
    
    # now add odd factors
    for i in range(3, int(math.sqrt(n)) + 1, 2):

        while n % i == 0:
            arr.append(i)
            n = n / i

    # if n is prime and greater than 2
    if n > 2:
        arr.append(n)
    
    return arr