import random
import concurrent.futures
import threading
import logging

SENTINEL = object()
logging.basicConfig(format='%(asctime)s: %(message)s', level=logging.INFO, datefmt='%H:%M:%S')


def producer(pipeline):
    for index in range(5):
        message = random.randint(1, 101)
        logging.info(f'producer got {message}')
        pipeline.set_message(message, 'producer')
    pipeline.set_message(SENTINEL, 'producer')


def consumer(pipeline):
    message = 0
    while message is not SENTINEL:
        message = pipeline.get_message('consumer')
        if message is not SENTINEL:
            logging.info(f'consume {message}')


class Pipeline:
    # pipeline allow only one message
    def __init__(self):
        self.message = 0
        self.producer_lock = threading.Lock()
        self.consumer_lock = threading.Lock()
        self.consumer_lock.acquire()

    def get_message(self, name):
        self.consumer_lock.acquire()
        message = self.message
        logging.info(f'{name} get message: {message}')
        # allow producer to set message
        self.producer_lock.release()
        return message

    def set_message(self, message, name):
        self.producer_lock.acquire()
        logging.info(f'{name} set message: {message}')
        self.message = message
        # allow consumer to get message
        self.consumer_lock.release()


if __name__ == '__main__':
    pipeline = Pipeline()
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(producer, pipeline)
        executor.submit(consumer, pipeline)
