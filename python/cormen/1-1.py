
'''
1-1 Comparison of running times
For each function f(n) and time t in the following table, determine the
largest size n of a problem that can be solved in time t, assuming that the
algorithm to solve the problem takes f(n) microseconds (edit: or whatever
second division is desired)

Times: 1 second, 1 minute, 1 hour, 1 day, 1 month, 1 year, 1 century
Functions: lg(n), n^1/2, nlog(n), n^2, n^3, 2^n, n!
'''

import math
import sys


class PrecisionError(BaseException):
    pass


def print_header():
    print('1 second,1 minute,1 hour,1 day,1 year,1 month,1 century')


def get_operation_windows(*, unit_factor=6):
    '''unit_factor dictates underlying metric temporal unit'''
    def sec_to_mis(x):
        try:
            if unit_factor > 0:
                base_time_chunk = 1*math.pow(10, unit_factor)
            else:
                raise PrecisionError
        except PrecisionError:
            print(
                'Error: the unit factor must be a natural number',
                file=sys.stderr
            )
        return x * base_time_chunk

    def min_to_mis(x):
        return 60 * sec_to_mis(x)

    def hrs_to_mis(x):
        return 60 * min_to_mis(x)

    def dys_to_mis(x):
        return 24 * hrs_to_mis(x)

    def mos_to_mis(x):
        return 30 * dys_to_mis(x)  # 30 is rounded average

    def yrs_to_mis(x):
        return 365 * dys_to_mis(x)  # 365 is rounded average

    def cns_to_mis(x):
        return 100 * yrs_to_mis(x)

    return [
        sec_to_mis(1), min_to_mis(1), hrs_to_mis(1), dys_to_mis(1),
        mos_to_mis(1), yrs_to_mis(1), cns_to_mis(1)
    ]


def get_bin_searcher(f, high_place_value=40):
    '''limited to integers which results in imprecision past ~10^12'''
    def calculator(period):
        high = math.pow(10, high_place_value)
        low = 0
        while True:
            mid = int((high + low)/2)

            if abs(high - low) <= 1:
                return round(mid)

            if f(mid) > period:
                high = mid
            else:
                low = mid
    return calculator


def build_binary_search_function(f):
    # extreme high-growth functions
    if f(10) > math.pow(10, 3):
        return get_bin_searcher(f, high_place_value=3)
    # extreme low-growth functions
    elif f(math.pow(10, 6)) - f(math.pow(10, 1)) < math.pow(10, 5):
        # skipping - growth too slow for a naive but accurate counting solution
        return lambda _: 'LOTS'
    else:
        return get_bin_searcher(f, high_place_value=20)


# =
# = Main
# =

'''
Note: I expected doing this programmatically to be a trivial exercise. It
proved the source of many frustrations. This has been a lesson in what
different orders of time complexity truly indicate: just like in physics with
the astonomical and quantum, the rules of very fast-growing functions are not
those of very slow-growing functions. The necessary accomodations for
various functions frustrates developing a simple, fast, and generic interface.
Even the stalwart binary search requires some situational tweaking because
of mathematical overflows.

I opted for a dispatcher to handle different cases, except for those functions
whose growth is so large I (at the time of writing this) lack a good method for
computationally solving them. Perhaps when armed with a fuller toolkit, I'll
rebuild this. In the meantime, an 'exam normal-form' solution will suffice.

n^1/2 => (10^6*c)^2 where c is 1 second, 60 seconds, 3600 seconds, etc.
lg(n) => 2^(10^6*c) where c is 1 second, 60 seconds, 3600 seconds, etc.
'''

# 6 determines f(n) is reckoned in microseconds
periods = get_operation_windows(unit_factor=6)
print_header()

fs = [
    lambda n: math.log2(n),
    lambda n: math.sqrt(n),
    lambda n: n,
    lambda n: n*math.log2(n),
    lambda n: math.pow(n, 2),
    lambda n: math.pow(n, 3),
    lambda n: math.pow(2, n),
    lambda n: math.factorial(n)
]

for f in fs:
    searcher = build_binary_search_function(f)
    for period in periods:
        print(f'{searcher(period)}', end='' if periods[-1] is period else ',')
    print()
