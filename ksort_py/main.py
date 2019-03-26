
import random
import math
import time

from ksort import ksort
from sort import algorithms


### Utils
def ordered(n):
    return list(range(n))

def unordered(n):
    return random.sample(ordered(n), n)

def partially_ordered(n, k):
    S = ordered(n)
    k = int(n*k)

    rand = random.sample(S, k)
    for a,b in zip(rand[0::2], rand[1::2]):
        S[a], S[b] = S[b], S[a]

    return S


def partially_sequential(n, k):
    S = []
    k = int(n*k)
    while len(S) < n:
        S += sorted(random.sample(range(n), k))

    return S[n//2:n] + S[:n//2]


def reasonable(n):
    S = []
    k = range( 2, int(math.log2(n) * n**(1/3)))
    while len(S) < n:
        S += sorted(random.sample(range(n), random.choice(k)))
    return S[n//2:n] + S[:n//2]


def arrays(n):
    yield 'Ordered:', ordered(n)

    for k in range(10, 70, 10):
        yield f'Part ord {k}:', partially_ordered(n, k/100.0)


    for k in range(10, 70, 10):
        yield f'Part Seq {k}:', partially_sequential(n, k/100.0)

    for k in range(6):
        yield 'Reasonable', reasonable(n)

    for _ in range(6):
        yield 'Unordered:', unordered(n)

    yield 'Reversed:', ordered(n)[::-1]


def average_time(alg, S):
    try:
        avg = 0
        for _ in range(100):
            t = time.clock_gettime_ns(0)
            alg(S)
            avg += time.clock_gettime_ns(0) -t
    except KeyboardInterrupt:
        raise
    except RecursionError:
        return -1

    return avg/100.0


def test(S):
    for name, alg in algorithms + [ ('KSort', ksort) ]:
        avg = average_time(alg, S[:])
        yield '{:>25,.2f}'.format(avg)


def test_all(title):
    for n in [ 10, 50, 100, 250, 500, 1000, 10000 ]:

        print('\n\n{:16s}{title}'.format('For N = %d'%n, title=title))
        for name, S in arrays(n):
            avgs = test(S)
            print('{:16s}: '.format(name) + '    '.join(avgs))



def main():
    title = '    '.join([ '{:>25s}'.format(name) for name, alg in algorithms + [('ksort', ksort)]])
    for i in range(10):
        print(f'##################### Test {i} #######################')
        test_all(title)



if __name__ == '__main__':
    main()
