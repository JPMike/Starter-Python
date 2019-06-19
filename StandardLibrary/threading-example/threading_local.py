import random
import threading
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s'
)


def show_value(data):
    try:
        val = data.value
    except AttributeError:
        logging.debug('no value yet')
    else:
        logging.debug('value={}'.format(val))


def worker(data):
    show_value(data)
    # value set to this thread
    data.value = random.randint(1, 100)
    show_value(data)


if __name__ == '__main__':
    # the attribute local_data.value is not present for any thread until it is set in that thread
    local_data = threading.local()
    show_value(local_data)
    # value set to main thread
    local_data.value = 1000
    show_value(local_data)

    for i in range(2):
        t = threading.Thread(target=worker, args=(local_data,))
        t.start()
