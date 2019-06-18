def test():
    L = [i for i in range(100)]


def f(x):
    return x ** 2


def g(x):
    return x ** 4


def h(x):
    return x ** 8


if __name__ == '__main__':
    import timeit

    # manual import test
    print(timeit.timeit("test()", setup="from __main__ import test"))
    # use globals to execute code within the current global namespace
    print(timeit.timeit("[func(42) for func in (f,g,h)]", globals=globals()))

    # use Timer to do the same task
    t = timeit.Timer('char in text', setup='text = "sample string"; char = "g"')
    print(t.timeit())
    # repeat time it
    print(t.repeat())
