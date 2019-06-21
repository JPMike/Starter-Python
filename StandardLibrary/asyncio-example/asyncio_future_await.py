import asyncio


def make_done(future, result):
    print(f'setting future result to {result}')
    future.set_result(result)


async def main(loop):
    all_done = asyncio.Future()

    print('scheduling mark_done')
    event_loop.call_soon(make_done, all_done, 'the result')

    result = await all_done
    print(f'returned result: {result}')


if __name__ == '__main__':
    event_loop = asyncio.get_event_loop()
    try:
        print('entering event loop')
        event_loop.run_until_complete(main(event_loop))
    finally:
        print('closing event loop')
        event_loop.close()
