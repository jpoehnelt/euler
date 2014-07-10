"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

def prime_factors(n):
    """
    finds all prime factors
    :param n: number to factor
    :return: list of prime factors
    """
    # base condition
    if n <= 3:
        return []
    f = []
    # find factors, skip 1 and n
    for i in range(2, int(n ** .5) + 1):
        if n % i == 0:
            # add if prime
            if len(prime_factors(i)) == 0:
                f.append(i)
            if len(prime_factors(n/i)) == 0 and n/i != i:
                f.append(n/i)

    return f

def problem_3(n=600851475143):
    return prime_factors(n)[-1]

if __name__ == "__main__":
    print problem_3()