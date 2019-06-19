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
    data.value = random.randint(1, 100)
    show_value(data)


class MyLocal(threading.local):
    # to initialize the setting so all threads start with the same value, use a subclass
    # and set the attributes in __init__()
    def __init__(self, value):
        super().__init__()
        logging.debug('initializing {}'.format(self))
        self.value = value


if __name__ == '__main__':
    local_data = MyLocal(1000)
    show_value(local_data)

    for i in range(2):
        # these threads have default value same as the main thread
        # __init__() is invoked on the same object
        t = threading.Thread(target=worker, args=(local_data,))
        t.start()

    # main thread value not change
    show_value(local_data)
