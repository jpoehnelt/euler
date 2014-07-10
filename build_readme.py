import timeit
import problems

# get answers
answers = []
with open('answers.txt', 'r') as f:
    for line in f.readlines():
        try:
            answers.append(line.split(' ')[1].strip())
        except IndexError:
            answers.append('')

# time and compare to answers
setup = 'import problems as p'
with open('README.md', 'w') as f:
    f.write('# Attempting Project Euler\n\n')
    for i in range(1, 477):
        try:
            problem = getattr(problems, 'problem_%d' % i)
            assert answers[i - 1] == str(problem())
            f.write(
                '- [x] Problem %d : %f ms\n' % (i, timeit.timeit("p.problem_%d" % i, setup=setup, number=1000) * 1000))
        except AssertionError:
            f.write('- [ ] Problem %d : Incorrect Answer\n' % i)
        except AttributeError:
            f.write('- [ ] Problem %d : Not Attempted\n' % i)


