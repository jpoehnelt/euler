def problem_5(n=100):
    sum_of_nums = 0
    sum_of_squares = 0
    for i in range(1,n+1):
        sum_of_nums += i
        sum_of_squares += i**2
    diff = abs(sum_of_squares - sum_of_nums**2)
    return diff


if __name__ == "__main__":
    print problem_5()
