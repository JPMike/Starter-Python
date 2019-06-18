import logging
import random
import threading
import time

logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s'
)


class Counter:
    def __init__(self, start=0):
        self.lock = threading.Lock()
        self.value = start

    def increment(self):
        logging.debug('waiting for lock')
        # get the lock, block here if did not got lock
        self.lock.acquire()
        try:
            logging.debug('acquired lock')
            self.value += 1
        finally:
            self.lock.release()


def worker(c):
    for i in range(2):
        pause = random.random()
        logging.debug('sleeping %0.02f', pause)
        time.sleep(pause)
        c.increment()
    logging.debug('done')


if __name__ == '__main__':
    counter = Counter()
    for i in range(2):
        t = threading.Thread(target=worker, args=(counter,))
        t.start()

    logging.debug('waiting for worker threads')
    main_thread = threading.main_thread()
    for t in threading.enumerate():
        if t is not main_thread:
            t.join()
    logging.debug('counter: {}'.format(counter.value))
