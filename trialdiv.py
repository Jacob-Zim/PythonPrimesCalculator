import math
import time
def prime(n):

    if n <= 1:
        return False
    
    # slightly heuristic - sqrt(n) will provide all the factors we need
    # as the factors will simply flip and repeat past that, therefore uneccessary to check
    for i in range(2, math.ceil(math.sqrt(n))):
        if n % i == 0:
            return False
    
    return True