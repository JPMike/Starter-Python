if __name__ == '__main__':
    import mmap
    import os

    mm = mmap.mmap(-1, 13)
    mm.write(b'hello world!')

    pid = os.fork()
    if pid == 0:
        print('in child process')
        mm.seek(0)
        print(mm.readline())
        mm.close()
    else:
        print('in father process')
