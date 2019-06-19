import logging
import threading
import time

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s (%(threadName)-2s) %(message)s'
)


def consumer(cond):
    logging.debug('starting consumer thread')
    with cond:
        cond.wait()
        logging.debug('resource is available to consumer')


def producer(cond):
    logging.debug('starting producer thread')
    with cond:
        logging.debug('making resource available')
        cond.notifyAll()


if __name__ == '__main__':
    # condition object is another way to synchronizing threads
    # allowing multiple threads to wait for the resource to be updated
    condition = threading.Condition()
    c1 = threading.Thread(name='c1', target=consumer, args=(condition,))
    c2 = threading.Thread(name='c2', target=consumer, args=(condition,))
    p = threading.Thread(name='p', target=producer, args=(condition,))
    c1.start()
    time.sleep(0.2)
    c2.start()
    time.sleep(0.2)
    p.start()
