import threading
import time
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s'
)


def delayed():
    logging.debug('worker running')


if __name__ == '__main__':
    # Timer is another way to subclass Thread
    t1 = threading.Timer(0.4, delayed)
    t1.setName('t1')
    t2 = threading.Timer(0.3, delayed)
    t2.setName('t2')

    logging.debug('starting timers')
    t1.start()
    t2.start()

    # cancel t2 before it start, so t2 never run
    logging.debug('waiting before canceling {}'.format(t2.getName()))
    time.sleep(0.2)
    logging.debug('canceling {}'.format(t2.getName()))
    t2.cancel()
    logging.debug('done')
    # t1 joined implicitly when the main thread is done here, since t1 is not daemon
