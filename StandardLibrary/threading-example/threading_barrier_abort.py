import threading
import time


def worker(barrier):
    print(threading.current_thread().name, 'waiting for barrier with {} others'.format(barrier.n_waiting))
    try:
        worker_id = barrier.wait()
    except threading.BrokenBarrierError:
        print(threading.current_thread().name, 'aborting')
    else:
        print(threading.current_thread().name, 'after barrier', worker_id)


if __name__ == '__main__':
    NUM_THREADS = 3
    # wait for one more thread
    barrier = threading.Barrier(NUM_THREADS + 1)
    threads = [threading.Thread(name='worker-{}'.format(i),
                                target=worker,
                                args=(barrier,))
               for i in range(NUM_THREADS)]
    for t in threads:
        print(t.name, 'starting')
        t.start()
        time.sleep(0.1)

    # wait more than actual threads, program never end, abort it, raise an exception in each blocked thread
    barrier.abort()

    for t in threads:
        t.join()
