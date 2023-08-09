class Link:
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest


def add(s, v):
    """Add v to an ordered list s with no repeats, returning modified s """
    if s.first > v:
        s.first, s.rest = v, Link(s.first, s.rest.rest)
    elif s.first < v and s.rest is Link.empty:
        s.rest = Link(v)
    elif s.first < v:
        add(s.rest, v)
    return s


class Tree:
    def __init__(self, label, branches=None):
        self.label = label

        if branches is None:
            branches = []
        for branch in branches:
            assert isinstance(branch, Tree)

        self.branches = list(branches)


def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 2) + fib(n - 1)


def count(f):
    def counted(n):
        counted.call_count += 1
        return f(n)

    counted.call_count = 0
    return counted


def memo(f):
    cache = {}

    def memoized(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]

    return memoized


def exp(b, n):
    if n == 0:
        return 1
    else:
        return b * exp(n, n - 1)


def exp_fast(b, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return square(exp_fast(b, n // 2))
    else:
        return b * exp_fast(b, n - 1)


square = lambda x: x * x


class Ratio:
    def __init__(self, m, n):
        self.numer = m
        self.denom = n

    def __repr__(self):
        return 'Ration({0}, {1})'.format(self.numer, self.denom)

    def __str__(self):
        return '{0}/{1}'.format(self.numer, self.denom)

    def __add__(self, other):
        if isinstance(other, int):
            numer = self.numer + other * self.denom
            denom = self.denom
        elif isinstance(other, Ratio):
            numer = self.numer * other.denom + self.denom * other.numer
            denom = self.denom * other.denom

        elif isinstance(other, float):
            return float(self) + other

        g = gcd(numer, denom)
        return Ratio(numer // g, denom // g)

    __radd__ = __add__

    def __float__(self):
        return self.numer / self.denom


def gcd(a, b):
    while a != b:
        a, b = min(a, b), abs(a - b)
    return a
