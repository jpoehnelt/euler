"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""


def prime_factors(n):
    # base condition
    if n <= 3:
        return set()
    f = set()
    # find factors, skip 1 and n
    for i in range(2, int(n ** .5) + 1):
        if n % i == 0:
            # add if prime
            if len(prime_factors(i)) == 0:
                f.add(i)
            if len(prime_factors(n/i)) == 0:
                f.add(n/i)

    return f

print prime_factors(600851475143)