import threading
import time
import logging


def worker():
    # get current thread name, which can be named when created
    print(threading.current_thread().getName(), 'Starting')
    # simulate to do something
    time.sleep(0.2)
    print(threading.current_thread().getName(), 'Exiting')


def my_worker():
    # user logging instead, config to print thread name
    logging.debug('Starting')
    time.sleep(0.3)
    logging.debug('Exiting')


# logging is thread safe
logging.basicConfig(
    level=logging.DEBUG,
    format='[%(levelname)s] (%(threadName)-10s) %(message)s'
)

if __name__ == '__main__':
    # named thread
    w = threading.Thread(name='worker', target=worker)
    my_w = threading.Thread(name='my_worker', target=my_worker)
    # not named thread
    default_worker = threading.Thread(target=worker)
    w.start()
    my_w.start()
    default_worker.start()
