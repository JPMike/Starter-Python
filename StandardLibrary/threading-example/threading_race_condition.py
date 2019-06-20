import logging
import concurrent.futures
import time

logging.basicConfig(format='%(asctime)s: %(message)s', level=logging.INFO, datefmt='%H:%M:%S')


class FakeDB:
    def __init__(self):
        self.value = 0

    def update(self, name):
        logging.info('thread {}: starting update'.format(name))
        local_copy = self.value
        local_copy += 1
        time.sleep(0.1)
        self.value = local_copy
        logging.info('thread {}: finishing update'.format(name))


if __name__ == '__main__':
    db = FakeDB()
    logging.info('testing update. staring value is {}'.format(db.value))
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        # max worker is 2, we submit 3 thread, two thread run at the same, race condition occur, value update is wrong
        # result suppose to be 3, get 2 instead
        for index in range(3):
            executor.submit(db.update, index)
    logging.info('testing update. staring value is {}'.format(db.value))
