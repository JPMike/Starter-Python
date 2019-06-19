import threading
import time


def worker(barrier):
    print(threading.current_thread().name, 'waiting for barrier with {} others'.format(barrier.n_waiting))
    # block here to wait for all threads to hit this point
    worker_id = barrier.wait()
    print(threading.current_thread().name, 'after barrier', worker_id)


if __name__ == '__main__':
    NUM_THREADS = 3
    barrier = threading.Barrier(NUM_THREADS)
    threads = [threading.Thread(name='worker-{}'.format(i),
                                target=worker,
                                args=(barrier,))
               for i in range(NUM_THREADS)]
    for t in threads:
        print(t.name, 'starting')
        t.start()
        time.sleep(0.1)

    for t in threads:
        t.join()
