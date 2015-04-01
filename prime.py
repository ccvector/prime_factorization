from __future__ import print_function
from collections import Counter

# def primes(last):
#     primes = []
#     for i in range(2, last):
#         is_prime = True
#         for j in primes:
#             if i % j == 0:
#                 is_prime = False
#         if is_prime:
#             primes.append(i)
#     return primes

def factors(x):
    factors = []
    i = 2
    while x > 1:
        if x % i == 0:
            x = x / i
            factors.append(i)
        else:
            i += 1
    return factors

def condense(factors):
    cnt = Counter()
    for factor in factors:
        cnt[factor] += 1
    condensed = []
    for k, v in cnt.items():
        condensed.append('{}^{}'.format(k, v))
    return condensed

def main():
    while True:
        x = input('Enter a positive integer greater than 1: ')
        if x > 1 and isinstance(x, int):
            print('{} = {}'.format(x, ' + '.join(condense(factors(x)))))
        else:
            print('Come on dude! Can you read?')
            continue

if __name__ == '__main__':
    main()
