import threading
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s'
)


def worker_with(lock):
    # lock implement the context manager API and are compatible with the with statement
    with lock:
        logging.debug('lock acquired via with')


def worker_no_with(lock):
    lock.acquire()
    try:
        logging.debug('lock acquired directly')
    finally:
        lock.release()


if __name__ == '__main__':
    lock = threading.Lock()
    w = threading.Thread(target=worker_with, args=(lock,))
    nw = threading.Thread(target=worker_no_with, args=(lock,))
    w.start()
    nw.start()
