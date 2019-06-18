import random
import threading
import time
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s'
)


def worker():
    pause = random.randint(1, 5)
    logging.debug('sleeping %0.2f', pause)
    time.sleep(pause)
    logging.debug('ending')


if __name__ == '__main__':
    for i in range(3):
        t = threading.Thread(target=worker, daemon=True)
        t.start()

    main_thread = threading.main_thread()
    # list all the threads
    for t in threading.enumerate():
        if t is main_thread:
            # do not join the main thread itself, deadlock will be caused
            continue
        logging.debug('joining {}'.format(t.getName()))
        t.join()
