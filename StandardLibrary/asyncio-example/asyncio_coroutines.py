import asyncio
import time


# 3 ways to actually run a coroutine
# 1. asyncio.run()
# 2. await
# 3. asyncio.create_task()

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def main():
    print(f"started at {time.strftime('%X')}")

    # way 2
    # run coroutine in order, need 3 seconds to finish
    await say_after(1, 'hello')
    await say_after(2, 'world')

    print(f"finished at {time.strftime('%X')}")

    print(f"started at {time.strftime('%X')}")
    # way 3
    # run coroutine concurrently as asyncio Tasks, needs 2 second to finish
    task1 = asyncio.create_task(say_after(1, 'hello'))
    task2 = asyncio.create_task(say_after(2, 'world'))

    await task1
    await task2

    print(f"finished at {time.strftime('%X')}")


if __name__ == '__main__':
    # way 1
    asyncio.run(main())
