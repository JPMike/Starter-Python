import logging
import threading
import time

logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s'
)


def wait_for_event(e):
    logging.debug('wait_for_event starting')
    # blocking here at e.wait()
    event_is_set = e.wait()
    logging.debug('event set: {}'.format(event_is_set))


def wait_for_event_timeout(e, t):
    # continue check is_set() to implement non blocking
    while not e.is_set():
        logging.debug('wait_for_event_timeout starting')
        # return after timeout, non blocking
        event_is_set = e.wait(2)
        logging.debug('event set: {}'.format(event_is_set))
        if event_is_set:
            logging.debug('processing event')
        else:
            logging.debug('doing other work')


if __name__ == '__main__':
    # signaling between threads
    # use event object to communicate between threads
    # event default to false
    e = threading.Event()
    t1 = threading.Thread(
        name='block',
        target=wait_for_event,
        args=(e,)
    )
    t1.start()

    t2 = threading.Thread(
        name='nonblock',
        target=wait_for_event_timeout,
        args=(e, 2)
    )
    t2.start()

    logging.debug('Waiting before calling Event.set()')
    time.sleep(0.3)
    # set event to true
    e.set()
    logging.debug('Event is set')
