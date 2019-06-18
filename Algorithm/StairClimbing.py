from functools import wraps
import unittest


def stair_climbing_cache(func):
    memory = {}

    @wraps(func)
    def wrapper(total_stairs):
        if total_stairs not in memory:
            value = func(total_stairs)
            memory[total_stairs] = value
        else:
            value = memory[total_stairs]
        return value

    return wrapper


# simple cache decorator to make the algorithm O(N)
@stair_climbing_cache
def stair_climbing(total_stairs):
    if total_stairs <= 1:
        # base case, exit condition of recursion
        return 1
    else:
        # recursive call: f(n) = f(n-1) + f(n-2)
        return stair_climbing(total_stairs - 1) + stair_climbing(total_stairs - 2)


class Test(unittest.TestCase):
    def test_stair_climbing(self):
        self.assertEqual(stair_climbing(total_stairs=4), 5)


if __name__ == "__main__":
    import timeit

    print(timeit.timeit("stair_climbing(total_stairs=4)", setup="from __main__ import stair_climbing"))
    unittest.main()
