import asyncio
import time


async def outer():
    # phase1 and phase2 must be executed in order
    print('in outer')
    print('waiting for result 1')
    # wait until return
    result1 = await phase1()
    print('waiting for result 2')
    result2 = await phase2(result1)
    return result1, result2


async def phase1():
    print('in phase1')
    time.sleep(0.5)
    return 'result1'


async def phase2(arg):
    print('in phase2')
    time.sleep(0.5)
    return f'result2 derived from {arg}'


if __name__ == '__main__':
    event_loop = asyncio.get_event_loop()
    try:
        return_value = event_loop.run_until_complete(outer())
        print(f'return value: {return_value}')
    finally:
        event_loop.close()
