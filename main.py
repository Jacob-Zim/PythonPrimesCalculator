import atkins
import eratosthenes
import sundarum

import fermats
import trialdiv

import factors

import time
import math

def timer(function):
    start = time.time()
    print(function)
    end = time.time()
    print('Calculation took '+(str(end - start))+' seconds')

print('Hey there!\n\nThis program can calculate whether a number is prime,\nfind the prime factors of a number,\nand sieve through the primes up to a given limit\n')


initial_input = ''
while initial_input not in {'p', 's', 'f', 'n'}: 
    initial_input = input('To start, let me know what you\'d like to do! \n(p for checking primality, s for sieve, or f for prime factors)\n')

    if initial_input[0] == 'p':
        test = ''
        while test not in {'t', 'f'}:
            test = input('I can check for primality with trial division or fermats little theorem \n(type t for trial division, f for fermats)\n')
            if test[0] == 't':
                number = ''
                while type(number) is not int:
                    number = input('Please type in an integer to find the primality of\n')
                    try:
                        number = abs(int(float(number)))
                    except:
                        number = ''
                    if type(number) is int:
                        timer(trialdiv.prime(number))
                        initial_input = input('\n Awesome! You can type n if you are done, otherwise hit any key to calculate something else!\n')

            if test[0] == 'f':
                number = ''
                while type(number) is not int:
                    number = input('Please type in an integer to find the primality of\n')
                    try:
                        number = abs(int(float(number)))
                    except:
                        number = ''
                    if type(number) is int:
                        timer(fermats.prime(number))
                        initial_input = input('\n Awesome! You can type n if you are done, otherwise hit any key to calculate something else!\n')

    if initial_input[0] == 's':
        test = ''
        while test not in {'a', 'e', 's'}:
            test = input('I can sieve out the primes up to a limit with sieve of Atkin, Eratosthenes, or Sundarum \n(type a for Atkin, e for Eratosthenes, or s for Sundarum)\n')

            if test[0] == 'a':
                number = ''
                while type(number) is not int:
                    number = input('Please type in an integer to sieve from with Atkin\n')
                    try:
                        number = abs(int(float(number)))
                    except:
                        number = ''
                    if type(number) is int:
                        timer(atkins.sieve(number))
                        initial_input = input('\n Awesome! You can type n if you are done, otherwise hit any key to calculate something else!\n')

            if test[0] == 'e':
                number = ''
                while type(number) is not int:
                    number = input('Please type in an integer to sieve from with Eratosthenes\n')
                    try:
                        number = abs(int(float(number)))
                    except:
                        number = ''
                    if type(number) is int:
                        timer(eratosthenes.sieve(number))
                        initial_input = input('\n Awesome! You can type n if you are done, otherwise hit any key to calculate something else!\n')
           
            if test[0] == 's':
                number = ''
                while type(number) is not int:
                    number = input('Please type in an integer to sieve from with Sundarum\n')
                    try:
                        number = abs(int(float(number)))
                    except:
                        number = ''
                    if type(number) is int:
                        timer(sundarum.sieve(number))
                        initial_input = input('\n Awesome! You can type n if you are done, otherwise hit any key to calculate something else!\n')
            
    if initial_input[0] == 'f':
        number = ''
        while type(number) is not int:
            number = input('Please type in an integer to find the prime factors of\n')
            try:
                number = abs(int(float(number)))
            except:
                number = ''
            if type(number) is int:
                timer(factors.prime_factors(number))
                initial_input = input('\n Awesome! You can type n if you are done, otherwise hit any key to calculate something else!\n')