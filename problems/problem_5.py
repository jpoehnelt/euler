def gcd(a, b):
    """Return greatest common divisor using Euclid's Algorithm."""
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    """Return lowest common multiple."""
    return a * b // gcd(a, b)


def problem_5():
    n = 2
    for i in xrange(3, 21):
        n = lcm(i, n)
    return n


if __name__ == "__main__":
    print problem_5()