import logging
import threading
import time

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s (%(threadName)-2s) %(message)s'
)


class ActivePool:
    # track which threads are able to run at a given moment
    def __init__(self):
        self.active = []
        self.lock = threading.Lock()

    def makeActive(self, name):
        with self.lock:
            self.active.append(name)
            logging.debug('running {}'.format(self.active))

    def makeInactive(self, name):
        with self.lock:
            self.active.remove(name)
            logging.debug('runing {}'.format(self.active))


def worker(s, pool):
    logging.debug('waiting to join the pool')
    with s:
        name = threading.current_thread().getName()
        pool.makeActive(name)
        time.sleep(0.1)
        pool.makeInactive(name)


if __name__ == '__main__':
    pool = ActivePool()
    # allow multiple threads to access shared resource concurrently, while still limiting the overall number
    # at most 2 are running concurrently
    # semaphore is one way to meet the goal
    s = threading.Semaphore(2)
    for i in range(4):
        t = threading.Thread(
            target=worker,
            name=str(i),
            args=(s, pool)
        )
        t.start()
