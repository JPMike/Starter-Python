from functools import lru_cache
from urllib.request import urlopen, build_opener, install_opener, ProxyHandler
from urllib.error import HTTPError

proxy_handler = ProxyHandler({})
opener = build_opener(proxy_handler)
install_opener(opener)


@lru_cache(maxsize=32)
def get_pep(num):
    resource = 'http://www.python.org/dev/peps/pep-%04d/' % num
    try:
        with urlopen(resource) as s:
            return s.read()
    except HTTPError:
        return 'Not Found'


@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


def get_pep_test():
    for n in [8, 290, 308, 320, 8, 218, 320, 279, 289, 320, 9991]:
        pep = get_pep(n)
        print(n, len(pep))
    print(get_pep.cache_info())


def lru_cache_test():
    print([fib(n) for n in range(10)])
    print(fib.cache_info())


if __name__ == '__main__':
    # lru_cache_test()
    # get_pep_test()
    pass
