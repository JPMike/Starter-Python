import asyncio
import time


async def eternity():
    await asyncio.sleep(3600)
    print('yay!')


async def foo():
    await asyncio.sleep(1)
    return 42


async def main():
    # wait for at most 1 seconds
    try:
        # if timeout is None, block until the future completes
        await asyncio.wait_for(eternity(), timeout=1.0)
    except asyncio.TimeoutError:
        print('timeout')

    task = asyncio.create_task(foo())
    done, pending = await asyncio.wait({task})
    if task in done:
        print('task is done')


if __name__ == '__main__':
    print(time.time())
    asyncio.run(main())
    print(time.time())
