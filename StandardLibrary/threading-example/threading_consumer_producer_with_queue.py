import concurrent.futures
import logging
import queue
import random
import threading
import time

logging.basicConfig(format='%(asctime)s: %(message)s', level=logging.INFO, datefmt='%H:%M:%S')


def producer(queue, event):
    while not event.is_set():
        message = random.randint(1, 101)
        logging.info(f'producer got message: {message}')
        queue.put(message)
    logging.info('producer received event. exiting')


def consumer(queue, event):
    while not event.is_set() or not queue.empty():
        message = queue.get()
        logging.info(f'consumer storing message: {message} size={queue.qsize()}')
    logging.info('consumer received event. exiting')


if __name__ == '__main__':
    # queue here is thread safe
    pipeline = queue.Queue(maxsize=10)
    # event flag default to false
    event = threading.Event()
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(producer, pipeline, event)
        executor.submit(consumer, pipeline, event)

        time.sleep(0.1)
        logging.info('main: about to set event')
        # set it to true
        event.set()
