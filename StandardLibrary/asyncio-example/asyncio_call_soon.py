import asyncio
import functools


def callback(arg, *, kwarg='default'):
    print(f'callback invoked with {arg} and {kwarg}')


async def main(loop):
    print('registering callbacks')
    # schedule a callback to be called with args arguments at the next iteration of the event loop
    loop.call_soon(callback, 1)
    wrapped = functools.partial(callback, kwarg='not default')
    loop.call_soon(wrapped, 2)
    await asyncio.sleep(0.5)


if __name__ == '__main__':
    event_loop = asyncio.get_event_loop()
    try:
        print('entering event loop')
        event_loop.run_until_complete(main(event_loop))
    finally:
        print('closing event loop')
        event_loop.close()
