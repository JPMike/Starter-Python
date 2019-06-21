import asyncio
import functools


def callback(future, n):
    print(f'{n}: future done: {future.result()}')


async def register_callbacks(all_done):
    print('registering callbacks on future')
    # the callback should expect one argument, the Future instance
    # to pass additional arguments to the callback, user partial to create a wrapper
    all_done.add_done_callback(functools.partial(callback, n=1))
    all_done.add_done_callback(functools.partial(callback, n=2))


async def main(all_done):
    # register callback function
    await register_callbacks(all_done)
    print('setting result of future')
    # callback function will be called after future is set
    all_done.set_result('the result')


if __name__ == '__main__':
    event_loop = asyncio.get_event_loop()
    try:
        all_done = asyncio.Future()
        print('entering event loop')
        event_loop.run_until_complete(main(all_done))
    finally:
        print('closing event loop')
        event_loop.close()
