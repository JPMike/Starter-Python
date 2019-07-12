import time


def echo(i):
    time.sleep(0.0001)


def test_multiprocess_pool():
    from multiprocessing import Pool
    p = Pool(10)
    run1 = [a for a in p.imap_unordered(echo, range(10))]
    run2 = [a for a in p.imap_unordered(echo, range(10))]
    run3 = [a for a in p.imap_unordered(echo, range(10))]
    run4 = [a for a in p.imap_unordered(echo, range(10))]

    print(run1 == run2 == run3 == run4)


def test_gevent_pool():
    from gevent.pool import Pool
    p = Pool(10)
    run1 = [a for a in p.imap_unordered(echo, range(10))]
    run2 = [a for a in p.imap_unordered(echo, range(10))]
    run3 = [a for a in p.imap_unordered(echo, range(10))]
    run4 = [a for a in p.imap_unordered(echo, range(10))]

    print(run1 == run2 == run3 == run4)


if __name__ == "__main__":
    test_multiprocess_pool()
    test_gevent_pool()
