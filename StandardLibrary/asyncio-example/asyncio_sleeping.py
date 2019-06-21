import asyncio
import datetime


async def display_date():
    loop = asyncio.get_running_loop()
    end_time = loop.time() + 5.0
    while True:
        print(datetime.datetime.now())
        if (loop.time() + 1.0) >= end_time:
            break
        # block for delay second
        # sleep() always suspends the current task, allowing other tasks to run
        await asyncio.sleep(1)


if __name__ == '__main__':
    asyncio.run(display_date())
