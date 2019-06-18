import threading


def worker(num):
    print('Working at {}'.format(num))


if __name__ == '__main__':
    threads = []
    for i in range(5):
        # make a Thread object
        t = threading.Thread(target=worker, args=(i,))
        threads.append(t)
        # start thread work
        t.start()
