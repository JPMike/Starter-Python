import threading

if __name__ == '__main__':
    lock = threading.Lock()
    print('first try: ', lock.acquire())
    # given zero timeout to prevent it from blocking
    print('second try: ', lock.acquire(0))

    # in a situation where separate code from the same thread needs to re-acquire the lock without blocking, use RLock
    rlock = threading.RLock()
    print('first try: ', rlock.acquire())
    print('second try: ', rlock.acquire())
