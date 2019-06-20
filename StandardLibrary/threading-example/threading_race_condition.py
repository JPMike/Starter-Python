import logging
import concurrent.futures
import time
import threading

logging.basicConfig(format='%(asctime)s: %(message)s', level=logging.DEBUG, datefmt='%H:%M:%S')


class FakeDB:
    def __init__(self):
        self.value = 0
        self._lock = threading.Lock()

    def update(self, name):
        logging.info('thread {}: starting update'.format(name))
        # simulate the process of read and write db
        # read from db and store in the local, all variables that are scoped to a function is thread safe
        local_copy = self.value
        local_copy += 1
        time.sleep(0.1)
        # write back to db
        self.value = local_copy
        logging.info('thread {}: finishing update'.format(name))

    def locked_update(self, name):
        logging.info('thread {}: starting update'.format(name))
        logging.debug(f"Thread {name} about to lock")
        # lock to solve race condition
        with self._lock:
            logging.debug(f"Thread {name} has lock")
            local_copy = self.value
            local_copy += 1
            time.sleep(0.1)
            self.value = local_copy
            logging.debug("Thread {} about to release lock".format(name))
        logging.debug(f"Thread {name} after release")
        logging.info('thread {}: finishing update'.format(name))


if __name__ == '__main__':
    db = FakeDB()
    logging.info('testing update. staring value is {}'.format(db.value))
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        # max worker is 2, we submit 3 thread, two thread run at the same, race condition occur, value update is wrong
        # result suppose to be 3, get 2 instead
        for index in range(3):
            executor.submit(db.update, index)
            # use locked update to solve race condition
            # executor.submit(db.locked_update, index)
    logging.info(f'testing update. staring value is {db.value}')
