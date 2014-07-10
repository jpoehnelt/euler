def problem_4():
    p = []
    for i in xrange(999, 99, -1):
        for j in xrange(i, 99, -1):
            product = i * j
            if is_palindrome(str(product)):
                p.append(product)
    return sorted(p)[-1]


def is_palindrome(x):
    if len(x) < 2:
        return True
    if x[0] == x[-1]:
        if is_palindrome(x[1:-1]):
            return True
    else:
        return False


if __name__ == "__main__":
    print problem_4()
