def collatz(n):
    ''' (int) -> sequence of ints

    Given any initial natural number n,
    prints out the sequence of positive integers
    generated by repeatedly following the rule:

    1. divide by two if the number is even or
    2. multiply by 3 and add 1 if the number is odd.

    >>> collatz(23)
    23
    70
    35
    106
    53
    160
    80
    40
    20
    10
    5
    16
    8
    4
    2
    1

    '''
    print(int(n))
    while not n == 1:
        if n % 2 == 0:
            n = n / 2
            print(int(n))
        else:
            n = n * 3 + 1
            print(int(n))
