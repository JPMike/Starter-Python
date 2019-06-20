import logging
import concurrent.futures
import time

logging.basicConfig(format='%(asctime)s: %(message)s', level=logging.INFO, datefmt='%H:%M:%S')


def thread_function(name):
    logging.info('thread {}: starting'.format(name))
    time.sleep(1)
    logging.info('thread {}: finishing'.format(name))


if __name__ == '__main__':
    # thread pool using context manager
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        # arguments pass by map
        executor.map(thread_function, range(3))
