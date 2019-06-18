import logging
import threading
import time

logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s'
)


def lock_holder(lock):
    logging.debug('starting')
    while True:
        lock.acquire()
        try:
            logging.debug('hoding')
            time.sleep(0.5)
        finally:
            logging.debug('not holding')
            lock.release()
        time.sleep(0.5)


def worker(lock):
    logging.debug('starting')
    num_tries = 0
    num_acquires = 0
    while num_acquires < 3:
        time.sleep(0.5)
        logging.debug('trying to acquire')
        # no blocking, return if timeout
        have_it = lock.acquire(0)
        try:
            num_tries += 1
            if have_it:
                logging.debug('iteration {}: acquired'.format(num_tries))
                num_acquires += 1
            else:
                logging.debug('iteration {}: not acquired'.format(num_tries))
        finally:
            if have_it:
                lock.release()
    logging.debug('done after {} iteration'.format(num_tries))


if __name__ == '__main__':
    lock = threading.Lock()
    holder = threading.Thread(
        target=lock_holder,
        args=(lock,),
        name='LockHolder',
        daemon=True
    )
    holder.start()
    worker = threading.Thread(
        target=worker,
        args=(lock,),
        name='Worker'
    )
    worker.start()
