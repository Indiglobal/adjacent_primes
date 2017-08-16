challenge_input = [270, 541, 993, 649]


def is_prime_brute(number, verbose=False):
    for n in range(2, number-1):
        if number % n == 0:
            output = '{} is divisible by {}.'.format(number, n)
            if verbose:
                print(output)
            return False

    output = '{} is prime.'.format(number)
    if verbose:
        print(output)
    return True


def is_prime_s(number, verbose=False):
    half = int(number / 2)
    for n in range(2, half+1):
        if n in primes or number % n == 0:

            output = '{} is divisible by {}.'.format(number, n)
            return False
    output = '{} is prime.'.format(number)
    if verbose:
        print(output)
    return True


def is_prime_s2(number, primes=[]):
    half = int(number / 2)
    # First check for division against out list of primes
    for n in primes:
        if number % n == 0:
            return False
    # Then carry on from the last known prime
    for n in range(primes[-1], half+1):
        if number % n == 0:
            return False
    return True


def nearest_primes(number, verbose=False):
    primes = []
    half = int(number / 2)
    # check if our number is prime, first time check all the numbers below our number as well
    for n in range(2, number-1):
        if is_prime_s2(n, primes=primes):
            primes.append(n)
    if is_prime_s2(number, primes=primes):
        print('{} is prime.')
    # number is not a prime so we start looking for the next lowest prime. This will be the last entry in our list.
    else:
        lower_prime = primes[-1]
        upper_prime = None
        n = number
        while upper_prime is None:
            n += n



    output = '{} < {} < {}'.format(lower_prime, number, upper_prime)
    print(output)


def is_prime_visual(number):
    primes_n = ''
    prime = True
    for n in range(2, number-1):
        if number % n == 0:
            primes_n += '.'
            prime = False
        else:
            primes_n += 'X'
    print('{} {} {}'.format(number, primes_n, prime))





'''max_n = 10000
primes = [is_prime_brute(i) for i in range(1, max_n)]
print(primes)
primes_s = [is_prime_s(i) for i in range(1, max_n)]
print(primes_s)
if primes == primes_s:
    print('Primes lists match!')
print(primes.count(True))
'''
