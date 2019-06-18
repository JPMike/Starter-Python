import threading
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s'
)


# make subclass of Thread
class MyThread(threading.Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs=None, *, daemon=None):
        # redefine constructor with the same signature
        # but make parent class private variable args and kwargs easy to access
        super().__init__(group=group, target=target, name=name,
                         daemon=daemon)
        self.args = args,
        self.kwargs = kwargs

    def run(self) -> None:
        # override run
        logging.debug('running with {} and {}'.format(self.args, self.kwargs))


if __name__ == '__main__':
    for i in range(3):
        t = MyThread(args=(i,), kwargs={'a': 'A', 'b': 'B'})
        t.start()
