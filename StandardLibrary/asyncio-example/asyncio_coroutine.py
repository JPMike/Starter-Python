import asyncio
import time


async def coroutine():
    print('in coroutine')
    time.sleep(1)
    print('about to return from coroutine')
    return 'result'


if __name__ == '__main__':
    event_loop = asyncio.get_event_loop()
    try:
        print('starting coroutine')
        coro = coroutine()
        print('entering event loop')
        # loop until the coroutine return
        return_value = event_loop.run_until_complete(coro)
        print(f'return value: {return_value}')
    finally:
        print('closing event loop')
        event_loop.close()
