import threading
import time
import logging


def daemon():
    logging.debug('Starting')
    time.sleep(0.2)
    print("daemon", file=open('threading_daemon_output.txt', 'a'))
    logging.debug('Exiting')


def non_daemon():
    logging.debug('Staring')
    print("non_daemon", file=open('threading_daemon_output.txt', 'a'))
    logging.debug('Exiting')


logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s'
)

if __name__ == '__main__':
    # daemon: run without blocking the main program from exiting
    d = threading.Thread(name='daemon', target=daemon, daemon=True)
    # default non daemon
    t = threading.Thread(name='non-daemon', target=non_daemon)
    d.start()
    t.start()
    # daemon thread not end before the main thread exit
    # let the main thread wait for the daemon thread to end
    # join will block the main thread indefinitely
    # if not join, daemon thread will be killed, and never complete the output
    d.join()
    # give join a expire time to stop blocking
    # d.join(0.1)
    # print('d.isAlive()', d.isAlive())
    t.join()
