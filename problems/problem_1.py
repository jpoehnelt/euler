def find_sum(n):
    """
    http://projecteuler.net/problem=1
    If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
    Find the sum of all the multiples of 3 or 5 below 1000.
    """
    return sum(i for i in range(n) if i % 3 == 0 or i % 5 == 0)


def problem_1(n=1000):
    return find_sum(n)


if __name__ == '__main__':
    print problem_1()
